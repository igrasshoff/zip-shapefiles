Zip Shapefile and Zip Direcotry of Shapefiles Python Script/Script Tool
---------------------------------------

Version: 1.03
ArcGIS Version: Tested on 10.3.1, but should work back to 10.0?
Created By: Ian Grasshoff
Created On: 3/22/2016
Modified On: N/A

License
-------
Copyright 2016 Waupaca County Land Information

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

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


