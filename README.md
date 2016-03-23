Purpose
--------
Simple, easy to use ArcGIS Script Tool or Python script to zip up a shapefile.  I found myself zipping shapefiles to upload to ArcGIS online quite regularly...this tool makes it a snap.  Also, I added arcpy as an optional import so the zipper.ShapefileZipper() class should work without arcpy (i.e. on a machine without ArcGIS).

Installation
------------
1.  Unzip the File - you are reading this so you probably unzipped :)
2.  Navigate to your Unzip location and Open up the Toolbox.tbx file using ArcGIS Desktop
3.  Modify the source property for the "Zip Shapefile" Script Tool -> Point it to the location of "ScriptToolZipSingleShapefile.py"
4. Modify the source property for the "Zip Directory of Shapefiles" Script Tool -> Point it to the location of "ScriptToolZipDirShapefiles.py"


Files Included
--------------

ScriptToolZipSingleShapefile.py
==========================
This is the interface between the zipper.py script and the "Zip Shapefile" ArcGIS Script Tool.  This will zip a single shapefile...


ScriptToolZipDirShapefile.py
==========================
This is the interface between the zipper.py script and the "Zip Directory of Shapefiles" ArcGIS Script Tool.  This will zip all shapefiles in a directory.  If you specify an output zip file name it will append all the shapefiles into a single zip.  If you don't specify a output zip file, then the tool will create individual zips for each shapefile it finds.


Toolbox.tbx
===========
Contains two ArcGIS Script Tools, one called "Zip Shapefile" and another called "Zip Directory of Shapefiles". There is also an example ArcGIS model so you can see how easy it is to use the scripts within model builder.


zipper.py
=========
This is the bulk of the tool logic.  It runs some basic file existence and file extension checks, then will zip up a shapefiles based on user inputs.


