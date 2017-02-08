#!/bin/bash

# This version of the run script will map a local directory to the /data
#  directory used by the container to render mapfiles.

if [[ ! -d $1 ]]; then
	echo "'$1' does not appear to be a directory. Please corrrect the path."
	exit 1
fi

# run a container that will be deleted on exit.
docker run -p 127.0.0.1:8000:80 --rm=true -v $1:/data --name gm3-demo-data gm3-demo-data 
