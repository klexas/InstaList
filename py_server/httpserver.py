import socket
import json
from types import SimpleNamespace

# TODO Read from a config file
server = '127.0.0.1'
port = 6969


with open('./common/settings.json') as f:
    settings = json.load(f)
    server = settings.hostname
    print(settings)

    port = settings.port
    print(settings)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server, port))
# Not really a socket when it needs a time to check. 
server_socket.listen(1)
print('Listening on port: %s ...' % port)

# While true..... Here be dragons - F* Python
# Try close this naturally (ctrl + x/c) 
# Python shouldnt be used for long running procs
# Functional only. "While true". I want to vomit
while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)
    # Basic intro, anyone who hits it now gets a 500 - Bad request
    response = 'HTTP/1.0 500 OK\n\nOkay boomer. '
    client_connection.sendall(response.encode())
    client_connection.close()

# Closing a socket makes it sound like a real socket - Very Java
# Anyway server dead
server_socket.close()


