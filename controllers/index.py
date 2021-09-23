import os
from pathlib import Path

from config.web import PROJECT_ROOT


class IndexController:

	def get_view(self):
		# Use the working directory, not project root
		# Using project root assumes too many hard coded relative paths from 'dev' root 
		view_file = os.path.join(os.getcwd(), 'view/index.html')
		view = Path(view_file).read_bytes()
		return view

	def get(self, req):
		return self.get_view()
