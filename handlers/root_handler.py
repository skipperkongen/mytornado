import tornado.web

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		return r'/'
		
	def initialize(self, message):
		self.message = message
		
	def get(self):
		self.write('Welcome to /. Message: %s' % self.message)
