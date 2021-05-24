ogr2ogr -f GeoJSON census_cities.geojson    tl_2019_27_place.shp        -nln census_cities -nlt POLYGON -spat -93.4  44.3  -92.9  44.7 -t_srs EPSG:4326
ogr2ogr -f GeoJSON census_roads.geojson     tl_2019_27_prisecroads.shp  -nln census_roads               -spat -93.4  44.3  -92.9  44.7 -t_srs EPSG:4326
ogr2ogr -f GeoJSON census_landmarks.geojson tl_2019_27_pointlm.shp      -nln census_landmarks           -spat -93.4  44.3  -92.9  44.7 -t_srs EPSG:4326

