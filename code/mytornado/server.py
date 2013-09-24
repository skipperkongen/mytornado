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

from mytornado.handlers.uptime import UptimeHandler

class MyTornadoServer(object):
	"""docstring for TornadoBase"""
		
	def __init__(self, options):
		super(MyTornadoServer, self).__init__()		
		
		settings = {
			"static_path": "%s/static" % (options.app),
			"template_path": "%s/templates" % (options.app)
		}
		
		# load handlers found in handler_path
		handlers = self.load_handlers("%s/handlers" % (options.app))
		for h in handlers:
			print "Found handler for: %s. Conf: %s" % (h[0], h[2])
			
		# register startup time for built-in uptime handler
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

		
	def load_handlers(self, handler_path):
		result = []
		# list python files in handler directory
		module_files = filter(lambda x: x.endswith('.py'), os.listdir( handler_path ))
		# load all handler classes found in files
		for module_file in module_files:
			# load file contents as python module
			head, tail = os.path.split( module_file )
			module_name, ext = os.path.splitext( tail )
			full_path = os.path.join(handler_path, module_file)
			module_obj = imp.load_source( 'mytornado.handlers.%s' % (module_name), full_path )
			# load configuration for handler module 
			module_conf = self.load_config_for_module( handler_path, module_name )
			for handler_name, handler_class in inspect.getmembers( module_obj ):
				# only load instances of tornado.web.RequestHandler
				if inspect.isclass(handler_class) and issubclass( handler_class, tornado.web.RequestHandler ):
					# create a tuple, part of list to be passed to Application constructor
					result.append(
						( module_conf[handler_name]['url_pattern'], handler_class, module_conf[handler_name] )
					)
		# return list of handler tuples 
		return result
	
	def load_config_for_module(self, handler_path, modulename):
		# find .conf file that matches handler module. File is in handlers directory
		config_file = os.path.join(handler_path, "%s.conf" % (modulename) )
		config = ConfigParser.ConfigParser()
		# read contents (INI file)
		config.read( config_file )
		config_dict = {}
		# load all sections into a dict. One section per handler class in module
		for section in config.sections():
			config_dict[section] = {}
			for option in config.options(section):
				config_dict[section][option] = config.get(section, option)
		# return config as dictionary
		return config_dict
		

		
		


