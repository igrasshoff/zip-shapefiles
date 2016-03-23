import zipper
import arcpy

try:
    input_dir = arcpy.GetParameterAsText(0)
    output_zipfile = arcpy.GetParameterAsText(1)
    zip_file_mode = arcpy.GetParameterAsText(2)
    shape_zipper = zipper.ShapefileZipper()
    result = shape_zipper.zip_shapefile_directory(input_dir, output_zipfile, zip_file_mode=zip_file_mode)
    if len(result) > 0:
        results = str(result)
        arcpy.SetParameterAsText(3, results)
        arcpy.AddMessage("!!!!!!!!!!!!!\n@@ SUCCESS @@\n!!!!!!!!!!!!!\nResult:  " + results)
    else:
        raise
except:
    arcpy.AddError("ZIP FILES NOT CREATED!")