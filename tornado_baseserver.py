import os
import inspect
import handlers

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
			print "Found handler %s" % (h[0]) 
		
		app = tornado.web.Application(
			handlers, **settings
		)		
		
		http_server = tornado.httpserver.HTTPServer(app)
		http_server.listen(options.port)
		tornado.ioloop.IOLoop.instance().start()
		print "Tornado server started on port %d" % (options.port)
		
	def load_handlers(self):
		result = []
		modules = filter (lambda (name,obj): inspect.ismodule(obj), inspect.getmembers(handlers))
		for name, obj in modules:
			for name2, obj2 in inspect.getmembers(obj):
				if inspect.isclass(obj2) and issubclass(obj2.__class__, tornado.web.RequestHandler.__class__):
					result.append((obj2.get_url_pattern(), obj2))
		return result

if __name__ == '__main__':
	server = TornadoBase()
		

		
		


