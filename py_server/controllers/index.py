from http.server import BaseHTTPRequestHandler
from pathlib import Path


class IndexController(BaseHTTPRequestHandler):

	def get_view(self):
		view = Path('view/index.html').read_text()
		return view

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes(self.get_view(), "utf-8"))
