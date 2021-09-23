# This is backwards. The controller should request what routes it needs. 
# The route doesn't care who wants it, its just information. This is bad tight coupling. 
# Factories and Injection 
# Maybe it's a preference, but abstraction is useful. 
from controllers.index import IndexController
from controllers.notfound import NotFoundController

# From the looks of it, this is a generic router, `Naming convention` 
#// I don't want to define all my routes in one place, right ?
class HomeRouter:
	def __init__(self):
		self.router = {}

	# I don't think I need to mention the problems here. Using self itelsf in the `set` seems super smelly. 
	# Maybe its an OO issue I have but the memory still is accessible if referecing itself to set something. 
	def set(self, path, handler):
		self.router[path] = handler

	def get(self, path): 
		# This looks cool handles the 404, but there is a condition, can we not build a hash map of routes (1 lvl controller) at startup time? 
		# This haskmap would also be locked down (you could lock up the set above)
		# I do appreciate no Exception handling too - Exceptions are expensive but I can think of a few here that might crash it all
		if path in self.router:
			return self.router[path]
		return NotFoundController()


# python is strange, but this is a very 'functional' way of doing things. 
# This looks like a constructor, but above you have one already with `__init_` ?
# What if I need some middleware to already have the route constraints ?
# Can we not have this an an encapuslated factory ? IE: 'LoadRoutes()' - Maybe python works different. 
MY_ROUTER = HomeRouter()
# The MY_ROUTER looks like some kind of global (c++ trauma) 
# Should this not be 'called' when the server is ready ? "Hey im ready for my controllers, 'for controllers: start up'". 
# #Maybe personal preference. But I like the boss being in charge of determining when the critical actions happen (or dont). 
MY_ROUTER.set("/", IndexController())