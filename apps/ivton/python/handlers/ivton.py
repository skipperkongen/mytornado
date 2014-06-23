import os

import tornado.web

class IvtonHandler(tornado.web.RequestHandler):
			
	def initialize(self, url_pattern, uploads_path):
		self.url_pattern = url_pattern
		self.uploads_path = uploads_path
	
	def get(self):
		self.render('ivton.html')
		
	def post(self):

		fileinfo = self.request.files['inputfile'][0]
		print "fileinfo is", fileinfo
		fname = fileinfo['filename']
		extn = os.path.splitext(fname)[1]
		cname = str(uuid.uuid4()) + extn
		fh = open(__UPLOADS__ + cname, 'w')
		fh.write(fileinfo['body'])
		self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)