import time
import datetime

import tornado.web

class UptimeHandler(tornado.web.RequestHandler):
		
	def initialize(self, startup_millis):
		self.startup_millis = startup_millis
		
	def get(self):
		current_millis = time.mktime(time.gmtime())
		diff_millis = current_millis - self.startup_millis
		delta = datetime.timedelta(seconds=diff_millis)
		self.write("uptime: %dd%ds" % (delta.days, delta.seconds))