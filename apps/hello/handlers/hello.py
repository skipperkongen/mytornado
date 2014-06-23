import tornado.web

class HelloHandler(tornado.web.RequestHandler):
			
	def initialize(self, url_pattern, message):
		self.url_pattern = url_pattern
		self.message = message
		
	def get(self):
		self.render('hello_index.html', message=self.message)
