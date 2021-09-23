import os
from http.server import BaseHTTPRequestHandler
from pathlib import Path

from routes.home import MY_ROUTER
from config.web import PROJECT_ROOT


class ReqHandler(BaseHTTPRequestHandler):

	# If you want to get assets, use the working dir. 
	# Some sanitization on the `asset` would be nice.
	# also seems this should be private 
	def __get_asset(self, asset):
		view_file = os.path.join(os.getcwd(), 'view/assets' + asset)
		view = Path(view_file).read_bytes()
		return view


	#default is public - this is cool
	def do_GET(self):
		self.send_response(200)
		if self.path.endswith(".html") or self.path.endswith("/"):
			self.send_header("Content-type", "text/html")
			self.end_headers()
			controller = MY_ROUTER.get(self.path)
			self.wfile.write(controller.get(self))
			return

		self.end_headers()
		# calling an internal method, this get_asset should be private
		self.wfile.write(self.__get_asset(self.path))
