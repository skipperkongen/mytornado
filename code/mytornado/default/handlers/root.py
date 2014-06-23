import tornado.web

from datetime import timedelta

class RootHandler(tornado.web.RequestHandler):
			
	def initialize(self, url_pattern, message):
		self.url_pattern = url_pattern
		self.message = message
		
	def get(self):
		self.render('root_index.html', message=self.message)
