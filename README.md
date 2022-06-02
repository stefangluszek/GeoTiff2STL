# GeoTiff2STL

Converts GeoTIFF files into STL ready for 3D printing.

## How to use

1. Download world population density data in 1km resolution from [here](https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_MT_GLOBE_R2019A/GHS_POP_E2015_GLOBE_R2019A_54009_1K/V1-0/GHS_POP_E2015_GLOBE_R2019A_54009_1K_V1_0.zip).
2. Uzip the file, you are mostly intrested in the .tif file
3. Use [GQIS](https://qgis.org/) to open the tif file
4. Use the QGIS `Raster->Extraction->Clip Raster by Extent` to clip the are you are interested in. Save the clipped are as a `.tif` file.
5. Convert the `.tif` file into `.stl` with: `python gtiff2stl.py clip.tif` which should create `clip.tif.stl`.

## TODO
There are some arbitrary constants in the `gtiff2stl.py` that worked well for me with `1km` resolution files and a targeted maximum height of 150mm.

## GeoTIFF data source
[ghsl.jrc.ec.europa.eu](https://ghsl.jrc.ec.europa.eu/download.php?ds=pop)

## Dependencies
[GDAL](https://gdal.org/index.html) and [Python GDAL bindings](https://gdal.org/api/python.html)

On Ubuntu the easiest way to install both GDAL and python bindings is to install [gdal-bin](https://packages.ubuntu.com/bionic/gdal-bin) and [python-gdal](https://packages.ubuntu.com/bionic/gdal-bin).

[numpy-stl](https://pypi.org/project/numpy-stl/)

## Useful links
* [Geoprocessing with Python using Open Source GIS](https://www.gis.usu.edu/~chrisg/python/2009/)
* [AutoGIS course](https://automating-gis-processes.github.io/2016/index.html)

## Sample
Shanghai population density:
![Shanghai](/scrots/shanghai.png)

## First results

### Stockholm
![Stockholm](/scrots/sthlm.jpg)

### New York
![NY](/scrots/ny.jpg)
