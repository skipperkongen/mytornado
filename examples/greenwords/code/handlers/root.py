import tornado.web

class GreenwordsRootHandler(tornado.web.RequestHandler):
	
	def initialize(self, url_pattern):
		self.url_pattern = url_pattern

	def get(self):
		self.redirect('/greenwords/signup')