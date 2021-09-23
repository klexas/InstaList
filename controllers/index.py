import os
from pathlib import Path

from config.web import PROJECT_ROOT


class IndexController:

	def get_view(self):
		# Use the working directory, not project root
		# Using project root assumes too many hard coded relative paths from 'dev' root 
		view_file = os.path.join(os.getcwd(), 'view/index.html')
		# // Always nervous when reading files directly in controllers  - Offshore it to a service 
		# // somewhere who can clean it. If you need to clean incoming traffic, 
		# it's better to do it in 1 place not depends on devs to search everwhere its happening. 
		view = Path(view_file).read_bytes()
		# Don't be afraid of data types, worth a validation (even your own, hint hint)
		return view

	def get(self, req):
		return self.get_view()
