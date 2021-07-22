import os
from pathlib import Path

from py_server.config.web import PROJECT_ROOT


class IndexController:

	def get_view(self):
		view_file = os.path.join(PROJECT_ROOT, 'py_server/view/index.html')
		view = Path(view_file).read_bytes()
		return view

	def get(self, req):
		return self.get_view()
