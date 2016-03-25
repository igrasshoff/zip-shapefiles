import zipper


def zip_shapefile_simple():
    try:
        ### Inputs
        input_shapefile = "C:\\Temp\\Shapefiles\\test.shp"  # this dir will be searched for shapefiles

        shape_zipper = zipper.ShapefileZipper()  # Create Instance of Class

        # By only passing an input file, an individual shapefilename.zip will be created
        # Existing zip file will be deleted if it matches the name of the new .zip to be created..
        results = shape_zipper.zip_shapefile(input_shapefile)
        # returns a string path to the .zip that was created

        if len(results) > 1:
            print("SUCCESS!  " + str(results))
        else:
            print("WARNING: SHAPEFILE NOT ZIPPED:  " + input_shapefile)
    except:
        print("ERROR:  BIG FAIL!")


def zip_shapefile_output_zip():
    try:
        ### Inputs
        input_shapefile = "C:\\Temp\\Shapefiles\\test.shp"  # this dir will be searched for shapefiles
        output_zip = "C:\\TEMP\\shapefiles\\myZip1.zip"

        shape_zipper = zipper.ShapefileZipper()  # Create Instance of Class

        # Existing zip file will be deleted if it matches the name of the new .zip to be created..
        results = shape_zipper.zip_shapefile(input_shapefile, output_zip)
        # returns a string path to the .zip that was created

        if len(results) > 1:
            print("SUCCESS!  " + str(results))
        else:
            print("WARNING: SHAPEFILE NOT ZIPPED:  " + input_shapefile)
    except:
        print("ERROR:  BIG FAIL!")


def zip_shapefile_output_zip_append():
    try:
        ### Inputs
        input_shapefile = "C:\\Temp\\Shapefiles\\test.shp"  # this dir will be searched for shapefiles
        output_zip = "C:\\TEMP\\shapefiles\\myZip2.zip"
        file_mode = 'a'  # this is append mode, so any shapefiles found will be appending to the C:\\TEMP\\myZip.zip,
        # Warning, using the append mode it's possible to append duplicate files into the .zip...

        shape_zipper = zipper.ShapefileZipper()  # Create Instance of Class

        results = shape_zipper.zip_shapefile(input_shapefile, output_zip, file_mode)
        # returns a string path to the .zip that was created

        if len(results) > 1:
            print("SUCCESS!  " + str(results))
        else:
            print("WARNING: SHAPEFILE NOT ZIPPED:  " + input_shapefile)
    except:
        print("ERROR:  BIG FAIL!")


def zip_dir_simple():
    try:
        ### Inputs
        input_dir = "C:\\TEMP\\Shapefiles"  # this dir will be searched for shapefiles

        shape_zipper = zipper.ShapefileZipper()  # Create Instance of Class

        # By just passing an input directory, individual shapefilename.zip's will be created
        # Existing zip files will be deleted if they match the name of the new .zip to be created..
        results = shape_zipper.zip_shapefile_directory(input_dir)
        # returns a list of zips that were created, or None if nothing run

        if results:
            print("SUCCESS!" + str(results))
        else:
            print("NO SHAPEFILES ZIPPED, MAYBE THERE AREN'T ANY WITHIN " + input_dir)
    except:
        print("BIG FAIL!")

def zip_dir_output_zip():
    try:
        ### Inputs
        input_dir = "C:\\TEMP\\Shapefiles"  # this dir will be searched for shapefiles
        output_zip = "C:\\TEMP\\Shapefiles\\myZipDir.zip"  # Any shapefiles located within the input directory will be appended into a single zip

        shape_zipper = zipper.ShapefileZipper() # Create Instance of Class

        # Existing zip files will be deleted if they match the name of the new .zip to be created..
        results = shape_zipper.zip_shapefile_directory(input_dir, output_zip)
        # returns a list of zips that were created

        if results:
            print("SUCCESS!" + str(results))
        else:
            print("NO SHAPEFILES ZIPPED, MAYBE THERE AREN'T ANY WITHIN " + input_dir)
    except:
        print("BIG FAIL!")

def zip_dir_output_zip_append():
    try:
        ### Inputs
        input_dir = "C:\\TEMP\\Shapefiles"  # this dir will be searched for shapefiles
        output_zip = "C:\\TEMP\\Shapefiles\\myZipDir2.zip"  # Any shapefiles located within the input directory will be appended into a single zip
        file_mode = 'a'  # this is append mode, so any shapefiles found will be appending to the C:\\TEMP\\myZip.zip,
        # Warning, using the append mode it's possible to append duplicate files into the .zip...

        shape_zipper = zipper.ShapefileZipper() # Create Instance of Class

        # Existing zip files will be deleted if they match the name of the new .zip to be created..
        results = shape_zipper.zip_shapefile_directory(input_dir, output_zip, file_mode)
        # returns a list of zips that were created

        if results:
            print("SUCCESS!" + str(results))
        else:
            print("NO SHAPEFILES ZIPPED, MAYBE THERE AREN'T ANY WITHIN " + input_dir)
    except:
        print("BIG FAIL!")


# call example functions for directories
# print("Call zip_dir_simple()")
zip_dir_simple()
print("Call zip_dir_output_zip()")
zip_dir_output_zip()
print("zip_dir_output_zip_append()")
zip_dir_output_zip_append()

# call example functions for single shapefiles
print("zip_shapefile_simple()")
zip_shapefile_simple()
print("zip_shapefile_output_zip()")
zip_shapefile_output_zip()
print("zip_shapefile_output_zip_append()")
zip_shapefile_output_zip_append()

