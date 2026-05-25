# Notes on converting between formats

The original files provided to GeoMoose arrived in Shapefile format.
This was the contemporary "universal" file format for most software at the time.

The following conversions and their steps can be found below.

## To GeoJSON

GDAL was used to convert the Shapefile to GeoJSON with the following command:

```
ogr2ogr -f GeoJSON ./parcels.geojson ./parcels.shp parcels -t_srs epsg:4326
```

## To GeoParquet

DuckDB was then used to convert to GeoParquet format.


```
INSTALL spatial;
LOAD spatial;

COPY (SELECT * FROM ST_Read('parcels.geojson'))
TO 'parcels.geoparquet'
WITH (FORMAT 'PARQUET');
```
