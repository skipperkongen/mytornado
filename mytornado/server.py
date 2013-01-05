import os
import inspect
import handlers
import ConfigParser

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)
define("baseuri", default='', help="base uri prefix for redirects, absolute urls etc", type=str)

class MyTornadoServer(object):
	"""docstring for TornadoBase"""
	
	baseuri = options.baseuri
	
	def __init__(self):
		super(MyTornadoServer, self).__init__()		
		
		tornado.options.parse_command_line()
		
		settings = {
			"static_path": os.path.join(os.path.dirname(__file__), "../static"),
			"template_path": os.path.join(os.path.dirname(__file__), "../templates")
		}
		
		handlers = self.load_handlers()
		print handlers
		for h in handlers:
			print "Found handler for: %s. Conf: %s" % (h[0], h[2])
		
		app = tornado.web.Application(
			handlers, **settings
		)		
		
		http_server = tornado.httpserver.HTTPServer(app)
		http_server.listen(options.port)
		print "Starting tornado server on port %d" % (options.port)
		tornado.ioloop.IOLoop.instance().start()

		
	def load_handlers(self):
		result = []
		handler_modules = filter(lambda (name, obj): inspect.ismodule(obj), inspect.getmembers(handlers))
		handler_modules = filter(lambda (name, obj): obj.__package__ == 'handlers', handler_modules)

		for modulename, module in handler_modules:
			# load config file 
			module_conf = self.load_config_for_module(modulename)
			print modulename
			for handlername, handlerclass in inspect.getmembers(module):
				if issubclass(handlerclass.__class__, tornado.web.RequestHandler.__class__):
					print "BULU",handlername, handlerclass
					result.append(
						(handlerclass.get_url_pattern(), handlerclass, module_conf.setdefault( handlername, {}) )
					)
		return result
	
	def load_config_for_module(self, modulename):
		config_file = os.path.join(os.path.dirname(__file__), "..", "handlers", "%s.conf" % (modulename) )
		config = ConfigParser.ConfigParser()
		config.read( config_file )
		config_dict = {}
		for section in config.sections():
			config_dict[section] = {}
			for option in config.options(section):
				config_dict[section][option] = config.get(section, option)
		
		return config_dict
		

		
		


