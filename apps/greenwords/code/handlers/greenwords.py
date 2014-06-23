import os.path
import sqlite3
import datetime
import re

import tornado.httpserver
import tornado.ioloop
import tornado.web

# http://stackoverflow.com/questions/386294/maximum-length-of-a-valid-email-address
MAX_EMAIL_ADDRESS_LENGTH = 254 
# http://stackoverflow.com/questions/9280260/how-to-prevent-sql-injection-of-post-e-mail-field-using-php-4
EMAIL_REGEX = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$'

class GreenwordsAPIHandler(tornado.web.RequestHandler):
	
	def initialize(self, url_pattern):
		self.url_pattern = url_pattern

	def get(self, method):
		self.write('Called %s' % method)

class GreenwordsIndexHandler(tornado.web.RequestHandler):
	
	def initialize(self, url_pattern):
		self.url_pattern = url_pattern

	def get(self):
		self.render('greenwords_index.html')

class GreenwordsPageHandler(tornado.web.RequestHandler):

		def initialize(self, url_pattern):
			self.url_pattern = url_pattern
			self.db_path = os.path.join(os.path.dirname(__file__), "..", "data", "registrations.db")
			
		def get(self, page):
				print page
				if page == "signup":
					self.render('greenwords_signup.html')
				elif page == "thankyou":
					email = self.get_argument('email')
					self.render('greenwords_thankyou.html',email=email)
				elif page == "errorsignup":
					email = self.get_argument('email')
					self.render('greenwords_errorsignup.html',email=email)
				else:
					self.redirect("signup")
					
		def post(self, page):
				# Get variables
				email = self.get_argument('email').strip()
				email = email[:MAX_EMAIL_ADDRESS_LENGTH]
				lead_from = "unknown"
				registration_date = str(datetime.datetime.now())
				print "DEBUG: %s" % (self.request.uri) 

				# Validate email				
				if re.match(EMAIL_REGEX, email):
					print "registering email: %s" % (email)
					conn = sqlite3.connect(self.db_path)
					c = conn.cursor()
					stm = "INSERT INTO notify_on_launch(email, lead_from, registration_date) VALUES ('%s','%s','%s')" % \
						(email, lead_from, registration_date)
					c.execute(stm)
					conn.commit()
					conn.close()
					# Redirect to thankyou
					self.redirect("thankyou?email=%s" %  (email))
				else:
					self.redirect('errorsignup?email=%s' % (email))