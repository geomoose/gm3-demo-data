#!/bin/bash

# run a container that will be deleted on exit.
docker run -p 127.0.0.1:8000:80 --rm=true -v ~/Projects/GeoMOOSE/gm3-demo-maps:/data --name gm3-demo-data gm3-demo-data 
