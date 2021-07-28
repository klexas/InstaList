class NotFoundController:

	def get(self, req):
		return bytes("NOT FOUND", "utf8")
