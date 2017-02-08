#!/bin/bash

# run a container that will be deleted on exit.
docker run -p 127.0.0.1:4000:80 --rm=true --name gm3-demo-data gm3-demo-data 
