from controllers.index import IndexController
from controllers.notfound import NotFoundController


class MyRouter:
	def __init__(self):
		self.router = {}

	def set(self, path, handler):
		self.router[path] = handler

	def get(self, path):
		if path in self.router:
			return self.router[path]
		return NotFoundController()


MY_ROUTER = MyRouter()
MY_ROUTER.set("/", IndexController())
