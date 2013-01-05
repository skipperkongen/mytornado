# Tornado-base-server

Tornado server that allows you to drop files with your handler code in a directory.

To register a handler, create a file in the handlers directory that contains your handler class. The handler class must have a static method called `get_url_pattern()` that returns a string.

## Example

`root_handler.py`:

```python
import tornado.web

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		return '/'
		
	def get(self):
		self.write('Welcome to /')
```