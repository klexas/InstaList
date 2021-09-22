import os
from http.server import BaseHTTPRequestHandler
from pathlib import Path

from py_server.config.routes import MY_ROUTER
from py_server.config.web import PROJECT_ROOT


class ReqHandler(BaseHTTPRequestHandler):

	def get_asset(self, asset):
		view_file = os.path.join(PROJECT_ROOT, 'py_server/view/assets' + asset)
		view = Path(view_file).read_bytes()
		return view

	def do_GET(self):
		self.send_response(200)
		if self.path.endswith(".html") or self.path.endswith("/"):
			self.send_header("Content-type", "text/html")
			self.end_headers()
			controller = MY_ROUTER.get(self.path)
			self.wfile.write(controller.get(self))
			return

		self.end_headers()
		self.wfile.write(self.get_asset(self.path))
