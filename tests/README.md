# Tests for MapServer Data Services

This is a small set of tests to ensure that all of the test 
data services are configured properly.  It's a pretty shallow set of tests:

* For layers with WMS services, ensure that a sample image is returned for
  web-mercator (EPSG:3857), UTM-15N (EPSG:26915), and WFS84 (EPSG:4326).

* For layers with WFS services, ensure that features are returned with 
  a basic BBOX query.

## Requirements

* Tests require python, nosetests, and requests.  

## Running

```
nosetests -v .
```
