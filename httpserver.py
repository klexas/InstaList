from http.server import HTTPServer
# I like this. As all my comments suggest, use more of this bespoke design. 
from config.web import get_http_config
# // Request handler should be a 'factory' 
# not something the HTTPSERVER module needs, let the factory look after that.
# That way if things change, you only need to change your factory. 
from reqhandler import ReqHandler

if __name__ == "__main__":
	(hostName, serverPort) = get_http_config()

	webServer = HTTPServer((hostName, serverPort), ReqHandler)
	print("Server started http://%s:%s" % (hostName, serverPort))

	# Try catch is expensive, are you looking for something important here ?
	# Ahh.. Python stuff - need a loop to focus it. Maybe put this into 'dev' mode ?
	# // as for prod, no idea myself, you know better.
	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	# Don't bother with this, you're gonna know when it fails. 
	print("Server stopped.")
