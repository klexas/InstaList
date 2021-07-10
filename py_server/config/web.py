import json


def get_http_config():
	with open('config/settings.json') as f:
		settings = json.load(f)
		server = settings["hostname"]
		port = int(settings["port"])
	return server, port
