#!/usr/bin/env python2

#
# Check to see what Mapfiles may or may not have
# tests written.
#

#
# The MIT License (MIT)
#
# Copyright (c) 2017 GeoMoose.org, Dan "Ducky" Little
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os.path

# this should import the local "test" package.
import test

IGNORE_MAPFILES = ['geomoose_globals.map', 'common_metadata.map', 'temp_directory.map']

def traverse_dir(path):
	global IGNORE_MAPFILES

	mapfiles = []
	for item in os.listdir(path):
		next_path = os.path.join(path, item)
		if(os.path.isdir(next_path)):
			mapfiles += traverse_dir(next_path)
		elif(os.path.isfile(next_path) and next_path[-4:] == '.map'):
			mf_name = os.path.split(next_path)[1]
			if(mf_name not in IGNORE_MAPFILES):
				mapfiles.append(next_path)

	return mapfiles

def get_tested_mapfiles():
	mapfiles = []
	for name in dir(test):
		if('Test' in name):
			item = getattr(test, name)
			if(hasattr(item, 'mapfile')):
				mapfiles.append(item.mapfile)
	return mapfiles
			
			

if(__name__ == "__main__"):
	# path tweaking to match what needs to go in test.py
	mapfile_names = [x.replace('..', '.') for x in traverse_dir('../')]
	tested_mapfiles = get_tested_mapfiles()
	# convert to a dict
	mapfiles = {}

	any_missing = False
	for mf_name in mapfile_names:
		if(mf_name not in tested_mapfiles):
			print 'MISSING TEST FOR:', mf_name
			any_missing = True


	if(not any_missing):
		print 'All mapfiles have tests.'
	
