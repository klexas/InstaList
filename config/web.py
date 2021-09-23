import json
import os
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent

# This is good, but if i am a dev, and I want to load a new custom config
# I have a problem. Make this private, create a public facing method, 
# with sanitisation on the JSON to match your schema etc
# This should be locked down HARD. 
def get_http_config():
	# 
	config_file = os.path.join(os.getcwd(), 'config/settings.json')
	with open(config_file) as f:
		# sketchy - No need to say why - see above
		settings = json.load(f)
		 # Be careful of this way of getting vars, `settings` can be overwritten externally. 
		 # # Python behaves in the enviornment, not in a `sandobox` or virtual one. Like Java ;P 
		 # point is, this is a pointer, in the sys, not some virtualised JVM. 
		 # https://towardsdatascience.com/how-does-python-work-6f21fd197888
		server = settings["hostname"]
		# same as above, but diff data. 
		port = int(settings["port"])

		
	return server, port
