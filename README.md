# Tornado-base-server

Tornado server template. When the server starts, it automatically detects handler classes in the `handlers` directory, and registers them with the tornado application.

I'm writing a lot of Tornado applications, and this repository contains a template that I was repeating across projects again and again.

## Requirements for handlers

To register a new handler, create a Python module file in the handlers directory that contains your handler class(es). Each module may contain any number of handlers, which will all be loaded when the server starts.

* Your handler class(es) must inherit from `tornado.web.RequestHandler`
* Each handler class must have a static method called `get_url_pattern()` that returns the URL pattern that the handler is responsible for
* You must include an import of your handler class in the `handlers.__init__.py` module, e.g. `from my_handler.py ìmport *`.

## Example handler

`handlers/__init__.py`:

```python
from root_handler import *
```

`handlers/root_handler.py`:

```python
import tornado.web

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		"""Required for the server to register the handler (will crash if this method is not implemented).
		Notice that it is a static method"""
		return r'/'
		
	def initialize(self, message):
		"""Only implement this method if you're using a config file that matches the module name."""
		self.message = message
		
	def get(self):
		self.write('Welcome to /. Message: %s' % self.message)
```

You can optionally supply a configuration file with the same filename as the handler module, but with a `.conf` extension.

`handlers/root_handler.conf`:

```
[RootHandler]
message=Hello, World
```

This will result in "Hello, World" being passed as the argument to the `message` parameter in the handlers `initialize` method. The section name `[RootHandler]` in the config file, matches the class name for the handler in the Python module.

## Multiple handlers in a single module

This is perfectly fine. You can also have several config sections, each matching a class in the module.