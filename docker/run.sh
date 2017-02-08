#!/bin/bash

# this version of the run script will run using the 
#  mapfiles checked out on the image that was
#  there upon creation time.

# run a container that will be deleted on exit.
docker run -p 127.0.0.1:8000:80 --rm=true --name gm3-demo-data gm3-demo-data 
