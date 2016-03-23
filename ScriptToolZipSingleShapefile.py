import zipper
import arcpy

try:
    input_shapefile = arcpy.GetParameterAsText(0)
    output_zipfile = arcpy.GetParameterAsText(1)
    zip_file_mode = arcpy.GetParameterAsText(2)
    shape_zipper = zipper.ShapefileZipper()
    result = shape_zipper.zip_shapefile(input_shapefile, output_zipfile, zip_file_mode=zip_file_mode)
    if result:
        arcpy.SetParameterAsText(3, result)
        arcpy.AddMessage("!!!!!!!!!!!!!\n@@ SUCCESS @@\n!!!!!!!!!!!!!\nResult:  " + result)
    else:
        arcpy.AddMessage("FILE NOT CREATED")
except:
    arcpy.AddError("Opps...something done broke.")