#!/usr/bin/env python2

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


import os
from unittest import TestCase, skip

import requests

class MapfileTest(TestCase):
	## Constructor.
	#
	#  @param mapServerUrl  The URL to the mapserver instance.
	#  @param dataDir       The directory in which the demo files are hosted.
	#
	def setUp(self):
		self.msUrl = os.environ.get('MAPSERVER_URL', 'http://localhost:8000/cgi-bin/mapserv')
		self.dataDir = os.environ.get('DEMO_DATA_DIR', '/data/')

	def getmap_request(self, mapfile, layers, proj, coords):
		params = {
			'SERVICE': 'WMS',
			'VERSION': '1.3.0',
			'REQUEST': 'GetMap',
			'FORMAT': 'image/png',
			'TRANSPARENT': 'true',
			'WIDTH': '512',
			'HEIGHT': '512',
			'CRS': proj,
			'BBOX': ','.join([str(x) for x in coords]),
			'MAP': self.dataDir+mapfile,
			'LAYERS': ','.join(layers)
		}

		return requests.get(self.msUrl, params=params)
	
	def _test_getmap(self, mapfile, layers, proj, coords):
		r = self.getmap_request(mapfile, layers, proj, coords)
		self.assertEqual(r.status_code, 200, 'Server returned error status: '+str(r.status_code))
		self.assertEqual(r.headers['Content-Type'], 'image/png', 'Failed to return image! '+r.headers['Content-Type']+'\n\n'+r.text)

	# section where there is known data.
	def get_webmerc_image(self, mapfile, layers):
		self._test_getmap(mapfile, layers, 'EPSG:3857', 
		                        [-10360222.497787995,5555734.300937268,
					 -10354785.914151212,5565231.601701702])

	# get a wgs84 image that in and or around minnesota
	def get_wgs84_image(self, mapfile, layers):
		self._test_getmap(mapfile, layers, 'EPSG:3857',
					[-93, 43, -92, 44])

	# Meta-function for performing a common set of WMS
	# tests aginast a specific mapfile and layers
	def _wms_test(self, mapfile, layers):
		self.get_webmerc_image(mapfile, layers)
		self.get_wgs84_image(mapfile, layers)


class WMSProxyTest(MapfileTest):
	mapfile = './demo/wms/wms_proxy.map'

	@skip
	def test_wms_proxy(self):
		"""
		Test the WMS Proxy Mapfile
		"""

		layers = ['mncomp', 'usgs_topo_large', 'usgs_topo_small', 
		          'usgs_imagery_large', 'usgs_imagery_small']

		for layer in layers:
			self._wms_test(self.mapfile, [layer])

class IniternationalizationTest(MapfileTest):
	mapfile = './demo/i18n/utf8_polys.map'

	def test_wms(self):
		"""
		Test Internationalization WMS
		"""
		self._wms_test(self.mapfile, ['testing'])

	#TODO: Port the old internationalization tests
	#      from GM2

class FireStationsTest(MapfileTest):
	mapfile = './demo/firestations/firestations.map'

	def test_wms(self):
		"""
		Test Firestations WMS
		"""
		self._wms_test(self.mapfile, ['fire_stations'])

class PipelinesTest(MapfileTest):
	mapfile =  './demo/pipelines/pipelines.map'

	def test_wms(self):
		"""
		Test Pipelines WMS
		"""
		self._wms_test(self.mapfile, ['pipelines'])


class ScalebarKmTest(MapfileTest):
	mapfile = './demo/scalebars/scalebar_kilometers.map'

	def test_wms(self):
		"""
		Scalebar (km) WMS
		"""
		self._wms_test(self.mapfile, ['scalebar_km'])


class ScalebarFeetTest(MapfileTest):
	mapfile = './demo/scalebars/scalebar_feet.map'

	def test_wms(self):
		"""
		Scalebar (ft) WMS
		"""
		self._wms_test(self.mapfile, ['scalebar_feet'])


class ScalebarMilesTest(MapfileTest):
	mapfile = './demo/scalebars/scalebar_miles.map'

	def test_wms(self):
		"""
		Scalebar (mi) WMS
		"""
		self._wms_test(self.mapfile, ['scalebar_mi'])



class BasemapTest(MapfileTest):
	mapfile = './demo/statedata/basemap.map'

	def test_wms(self):
		"""
		Test basemap WMS
		"""
		layers = ['city_poly', 'county_borders']
		for layer in layers:
			self._wms_test(self.mapfile, [layer])

class ParcelTests(MapfileTest):
	mapfile = './demo/parcels/parcels.map'
	# Test for the WMS Proxy

	# Test the Parcel 
	def testing_parcel_wms_layers(self):
		"""
		Test Parcel Polygons
		"""
		mapfile = './demo/parcels/parcels.map'
		layers = ['parcels', 'parcels_points']
		for layer in layers:
			self._wms_test(mapfile, [layer])

