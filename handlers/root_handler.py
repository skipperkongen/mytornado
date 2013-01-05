import tornado.web
import tornado.options
import mytornado

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		return r'/'
		
	def initialize(self, message):
		self.message = message
		
	def get(self):
		self.render('index.html', message=self.message, uri=self.request.uri, baseuri=tornado.options.baseuri)
