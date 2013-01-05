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

class TornadoBase(object):
	"""docstring for TornadoBase"""
	def __init__(self):
		super(TornadoBase, self).__init__()
		
		tornado.options.parse_command_line()
		
		settings = {
			"static_path": os.path.join(os.path.dirname(__file__), "static"),
			"template_path": os.path.join(os.path.dirname(__file__), "templates")
		}
		
		handlers = self.load_handlers()
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
		handler_submodules = filter (lambda (name,obj): inspect.ismodule(obj) and name != "__init__", inspect.getmembers(handlers))
		for modulename, module in handler_submodules:
			# load config file 
			module_conf = self.load_config_for_module(modulename)
			for handlername, handlerclass in inspect.getmembers(module):
				if inspect.isclass(handlerclass) and issubclass(handlerclass.__class__, tornado.web.RequestHandler.__class__):
					result.append(
						(handlerclass.get_url_pattern(), handlerclass, module_conf.setdefault( handlername, {}) )
					)
		return result
	
	def load_config_for_module(self, modulename):
		config_file = os.path.join(os.path.dirname(__file__), "handlers", "%s.conf" % (modulename) )
		config = ConfigParser.ConfigParser()
		config.read( config_file )
		config_dict = {}
		for section in config.sections():
			config_dict[section] = {}
			for option in config.options(section):
				config_dict[section][option] = config.get(section, option)
		
		return config_dict

if __name__ == '__main__':
	server = TornadoBase()
		

		
		


