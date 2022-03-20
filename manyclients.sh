#!/bin/bash

# Create 150 clients to connect to the server
for N in {1..150}
do
	python3 basicClient.py $@ &
done
wait
