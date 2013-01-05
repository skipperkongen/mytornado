import tornado.web

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		return r'/'
		
	def get(self):
		self.write('Welcome to /')
