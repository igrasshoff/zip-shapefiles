##PURPOSE

Simple, easy to use ArcGIS Script Tool or Python script to zip up a shapefile.  I found myself zipping shapefiles to upload to ArcGIS online quite regularly...this tool makes it a snap.  Also, I added arcpy as an optional import so the zipper.ShapefileZipper() class should work without arcpy (i.e. on a machine without ArcGIS).

##ARCGIS TOOLBOX SETUP

1.  Unzip the File - you are reading this so you probably unzipped :)
2.  Navigate to your Unzip location and Open up the Toolbox.tbx file using ArcGIS Desktop
3.  Modify the source property for the "Zip Shapefile" Script Tool -> Point it to the location of "ScriptToolZipSingleShapefile.py"
4.  Modify the source property for the "Zip Directory of Shapefiles" Script Tool -> Point it to the location of "ScriptToolZipDirShapefiles.py"


##FILES INCLUDED

######example_usage.py
Example use cases of the zipper module.

######ScriptToolZipSingleShapefile.py
This is the interface between the zipper.py script and the "Zip Shapefile" ArcGIS Script Tool.  This will zip a single shapefile...


######ScriptToolZipDirShapefile.py
This is the interface between the zipper.py script and the "Zip Directory of Shapefiles" ArcGIS Script Tool.  This will zip all shapefiles in a directory.  If you specify an output zip file name it will append all the shapefiles into a single zip.  If you don't specify a output zip file, then the tool will create individual zips for each shapefile it finds.


######Toolbox.tbx
Contains two ArcGIS Script Tools, one called "Zip Shapefile" and another called "Zip Directory of Shapefiles". There is also an example ArcGIS model so you can see how easy it is to use the scripts within model builder.


######zipper.py
This is the bulk of the tool logic.  It runs some basic file existence and file extension checks, then will zip up a shapefiles based on user inputs.

##USAGE

**For complete usage examples please see example_usage.py**

```import zipper
shape_zipper = zipper.ShapefileZipper() # Create Instance of class
result_dir = shape_zipper.zip_shapfile_directory("C:\\Temp")  # Zips All Shapefiles found in C:\\TEMP
result_single = shape_zipper.zip_shapefile("C:\\Temp\\test.shp")  # Zips Single Shapefile C:\\Temp\\test.shp to C:\\Temp\\test.zip
```

##LICENSE

MIT License

Copyright (c) 2016 Ian Grasshoff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


