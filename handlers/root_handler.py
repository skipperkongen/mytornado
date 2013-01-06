import tornado.web

from datetime import timedelta

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		return r'/'
		
	def initialize(self, message):
		self.message = message
		
	def get(self):
		self.render('root_index.html', message=self.message)
