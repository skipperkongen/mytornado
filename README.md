# MyTornady

> MyTornady reduces the amount of boiler plate code needed for writing a Tornado app

## Quick start

Clone the MyTornado repository:

```bash
git clone git@github.com:skipperkongen/mytornado.git
```

Enter directory and run hello world example (assumes you have python and tornado installed)

```bash
cd mytornady/code
python start_server.py
```

Open browser and check that it is running

```
# displays "Hello, World"
open http://localhost:8080
```

Display help message for mytornado:

```bash
python start_server.py --help
```

## Rollin' your own

Create a new directory for your app:

```
mkdir yarr
cd yarr
```

A MyTornado app consists of three subdirectories. Create these:

```
mkdir handlers  # holds Python handler code
mkdir templates  # hold HTML templates
mkdir static  # holds css and images
```

Create a handler (handlers/yarr.py):

```python
import tornado.web

class YarrHandler(tornado.web.RequestHandler):
			
	def initialize(self, url_pattern, message):
		self.url_pattern = url_pattern
		self.message = message
		
	def get(self):
		self.render('hello_index.html', message=self.message)

```

Create a style sheet (static/style.css):

```
body {
	background-color: SeaGreen;
	color: SeaShell;
}
``` 

Start your app:

```
python start_server.py --app=PATH/TO/myapp
```

