import os

from tornado.options import define, options, parse_command_line

from mytornado.server import Server

define("port", default = 8080, help="run on the given port", type = int)
define(
	"app", 
	default = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apps", "hello"), 
	help = "directory that contains the handlers/templates/static subdirectories", 
	type = str
)

if __name__ == '__main__':
	parse_command_line()
	Server( options )
