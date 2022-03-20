#!/bin/bash

# Create 50 clients to connect to the server
for N in {1..50}
do
	python3 basicClient.py &
done
wait
