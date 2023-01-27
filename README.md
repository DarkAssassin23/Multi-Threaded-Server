# Multi-threaded server

About
----------------
This is a basic multi-threaded TCP server written in C, along with a client
script to connect to it. 

This server takes in the name of a file the user inputs and returns the
contents back to the user. 

Building and Deploying with Docker
----------------
You can build and deploy this server with docker. To build the docker image
use the provided <code>Dockerfile</code>.
```bash
docker build -t server .
```

Once you build the docker image you can run it with the following command
```bash
docker run -d -p 8989:8989 server
```
