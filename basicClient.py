#!/usr/bin/python3

import socket, ipaddress, sys, time, random

# Default host and port to connect to
HOST = "127.0.0.1"
PORT = 8989


# Checks if IP Address passed in is valid
def validIP(ip):
	bits = ip.split('.')
	if(len(bits)>4 or len(bits)<4):
		return False
	for x in bits:
		if(x.isdigit()):
			if(int(x)>255):
				return False
			elif(not x.isdigit()):
				return False
	return True

# Checks if the Port number passed in is Valid
def validPort(port):
	if(not port.isdigit()):
		return False
	if(int(port)<0 or int(port)>65535):
		return False
	return True

if(len(sys.argv)>2):
	if(validIP(sys.argv[1])):
		HOST = sys.argv[1]
	if(validPort(sys.argv[2])):
		PORT = (int)(sys.argv[2])
elif(len(sys.argv)>1):
	if(validIP(sys.argv[1])):
		HOST = sys.argv[1]
	
filesToRequest = ["makefile", "server.c", "queue.c", "queue.h"]
# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Time took to recieve data
start = time.time()

# Connect to socket
sock.connect((HOST, PORT))

# Create and send message
fileToRequest = random.randint(0,len(filesToRequest)-1)
data = filesToRequest[fileToRequest]+"\n"
data = data.encode()
sock.sendall(data)

# Recieve and decode response
data = sock.recv(4096)
msg = data.decode()

# Print out response
#print(msg)

# Close connection
sock.close()

end = time.time() - start

print("Time Elapsed: "+str(end)+", file requested: "+filesToRequest[fileToRequest])
