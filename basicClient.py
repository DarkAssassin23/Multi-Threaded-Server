#!/usr/bin/python3

import socket

# Host and port to connect to
HOST = "127.0.0.1"
PORT = 8989

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to socket
sock.connect((HOST, PORT))

# Create and send message
data = "makefile\n"
data = data.encode()
sock.sendall(data)

# Recieve and decode response
data = sock.recv(4096)
msg = data.decode()

# Print out response
print(msg)

# Close connection
sock.close()
