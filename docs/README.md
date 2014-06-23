# Tornado-base-server

Tornado server template. When the server starts, it automatically detects handler classes in the `handlers` directory, and registers them with the tornado application.

I'm writing a lot of Tornado applications, and this repository contains a template that I was repeating across projects again and again.

## Requirements for handlers

To register a new handler, create a Python module file in the handlers directory (configure with `--handlers_path=XXX` command line option) that contains your handler class(es). Each Python module in directory may contain any number of handlers, which will all be loaded when the server starts.

* Your handler class(es) must inherit from `tornado.web.RequestHandler`
* Each handler class must have a static method called `get_url_pattern()` that returns the URL pattern that the handler is responsible for

You can optionally create a configuration file with the same filename as the handler module, but with a `.conf` extension. This file must be in the same directory used for handlers. It should contain a section for each class that has a configuration (see example below).

## Example handler

`handlers/root_handler.py`:

```python
import tornado.web

class RootHandler(tornado.web.RequestHandler):
	
	@staticmethod
	def get_url_pattern():
		"""You handler class must implement this method. Notice that it is a static method"""
		return r'/'
		
	def initialize(self, message):
		"""(Optional) you must implement this method if you're using a config file that 
		matches the module name (see config example below)."""
		self.message = message
		
	def get(self):
		self.write('Welcome to /. Message: %s' % self.message)
```

`handlers/root_handler.conf`:

```
[RootHandler]
message=Hello, World
```

This will result in "Hello, World" being passed as the argument to the `message` parameter in the handlers `initialize` method. 

The section name `[RootHandler]` in the config file, must match the class name for the handler in the Python module.

## Multiple handlers in a single module

This is perfectly fine. You can also have several config sections, each matching a class in the module.