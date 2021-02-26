# Data Description


## census.gpkg


### Source


The `census.gpkg` is a GeoPackage containing the following U.S. Census Bureau TIGER files for Minnesota:

- Polygon (Places): ftp://anonymous@ftp2.census.gov/geo/tiger/TIGER2019/PLACE/tl_2019_27_place.zip
- Line (Primary and Secondary Roads):  ftp://anonymous@ftp2.census.gov/geo/tiger/TIGER2019/PRISECROADS/tl_2019_27_prisecroads.zip
- Point (Point Landmark): ftp://anonymous@ftp2.census.gov/geo/tiger/TIGER2019/POINTLM/tl_2019_27_pointlm.zip


### Processing

The data was coverted from shapefile to GeoPackage using GDAL's ogr2ogr command line:
```
ogr2ogr -f GPKG census_full.gpkg tl_2019_27_place.shp       -nln census_cities_gpkg -nlt POLYGON
ogr2ogr -f GPKG census_full.gpkg tl_2019_27_prisecroads.shp -nln census_roads_gpkg      -update
ogr2ogr -f GPKG census_full.gpkg tl_2019_27_pointlm.shp     -nln census_landmarks_gpkg  -update
ogr2ogr -f GPKG -spat -93.4  44.3  -92.9  44.7 census.gpkg census_full.gpkg
```

