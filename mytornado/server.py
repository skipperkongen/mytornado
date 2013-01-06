import os
import imp
import inspect
import ConfigParser
import time
import datetime

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import mytornado.handlers

from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)
define("handler_path", default=os.path.join(os.path.dirname(__file__), "../handlers"), help="path to directory that holds handlers", type=str)
define("template_path", default=os.path.join(os.path.dirname(__file__), "../templates"), help="path to directory that holds templates", type=str)
define("static_path", default=os.path.join(os.path.dirname(__file__), "../static"), help="path to directory that holds static files", type=str)

class UptimeHandler(tornado.web.RequestHandler):
		
	def initialize(self, startup_millis):
		self.startup_millis = startup_millis
		
	def get(self):
		current_millis = time.mktime(time.gmtime())
		diff_millis = current_millis - self.startup_millis
		delta = datetime.timedelta(seconds=diff_millis)
		self.write("uptime: %dd%ds" % (delta.days, delta.seconds))

class MyTornadoServer(object):
	"""docstring for TornadoBase"""
		
	def __init__(self):
		super(MyTornadoServer, self).__init__()		
		
		tornado.options.parse_command_line()
		
		settings = {
			"static_path": os.path.join(os.path.dirname(__file__), options.static_path),
			"template_path": os.path.join(os.path.dirname(__file__), options.template_path)
		}
		
		handlers = self.load_handlers()
		for h in handlers:
			print "Found handler for: %s. Conf: %s" % (h[0], h[2])
			
		# register startup time for uptime handler
		startup_millis = time.mktime(time.gmtime())
		handlers.append(
			(r'/mytornado/uptime', UptimeHandler, {'startup_millis': startup_millis})
		)
		
		app = tornado.web.Application(
			handlers, **settings
		)		
		
		http_server = tornado.httpserver.HTTPServer(app,xheaders=True)
		http_server.listen(options.port)
		print "Starting tornado server on port %d" % (options.port)
		tornado.ioloop.IOLoop.instance().start()

		
	def load_handlers(self):
		result = []
		# list python files in handler directory
		module_files = filter(lambda x: x.endswith('.py'), os.listdir(options.handler_path))
		for module_file in module_files:
			head, tail = os.path.split(module_file)
			module_name, ext = os.path.splitext(tail)
			full_path = os.path.join(options.handler_path, module_file)
			print "DEBUG", head, tail, module_name, ext, module_file
			module_obj = imp.load_source('mytornado.handlers.%s' % (module_name), full_path)
			# create tuple
			module_conf = self.load_config_for_module( module_name )
			for handler_name, handler_class in inspect.getmembers( module_obj ):
				if inspect.isclass(handler_class) and issubclass(handler_class, tornado.web.RequestHandler):
					print "DEBUG2", handler_name, handler_class 
					result.append(
						( module_conf[handler_name]['url_pattern'], handler_class, module_conf[handler_name] )
					)

		return result
	
	def load_config_for_module(self, modulename):
		config_file = os.path.join(options.handler_path, "%s.conf" % (modulename) )
		config = ConfigParser.ConfigParser()
		config.read( config_file )
		config_dict = {}
		for section in config.sections():
			config_dict[section] = {}
			for option in config.options(section):
				config_dict[section][option] = config.get(section, option)
		
		return config_dict
		

		
		


