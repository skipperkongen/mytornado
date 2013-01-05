# Tornado-base-server

Tornado server template. When the server starts, it automatically detects handler classes in the `handlers` directory, and registers them with the tornado application.

To register a handler, create a file in the handlers directory that contains your handler class(es). Each handler class must have a static method called `get_url_pattern()`. The handler will be assigned by tornado to listen for requests on that url.

I'm writing a lot of Tornado applications, and this repository contains a template that I was repeating across projects again and again.

## Example handler

`handlers/root_handler.py`:

```python
import tornado.web

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		return '/'
		
	def get(self):
		self.write('Welcome to /')
```