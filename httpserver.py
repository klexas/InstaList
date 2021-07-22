from http.server import HTTPServer

from py_server.config.web import get_http_config
from py_server.controllers.index import IndexController

if __name__ == "__main__":
	(hostName, serverPort) = get_http_config()
	webServer = HTTPServer((hostName, serverPort), IndexController)
	print("Server started http://%s:%s" % (hostName, serverPort))

	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	print("Server stopped.")
