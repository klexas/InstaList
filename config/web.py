import json
import os
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent


def get_http_config():
	config_file = os.path.join(os.getcwd(), 'config/settings.json')
	with open(config_file) as f:
		settings = json.load(f)
		server = settings["hostname"]
		port = int(settings["port"])
	return server, port
