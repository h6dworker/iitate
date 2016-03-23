#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"

Project_mxd = env.workspace + '\\' + 'H24_20_AM_Measure.mxd'
field_name = "GRID_NAME"
##Project_mxd = env.workspace + '\\' + 'Enlarge_H24_20_AM_Measure.mxd'
##field_name = "GRID_LARGE"
path_name = "20"

mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]

# Select_Grid_shp = r"D:\IITATE\IITATE_Phase1\Shape\Point_shape\survey_point.shp"
Point_st_lyr = arcpy.mapping.ListLayers(mxd,"STATIONNO", df)[0]
Point_st_lyr.visible = True

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("GRID_NAME")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(field_name)

    Point_lyr_1 = str(target_grid)
##    Point_st_lyr.replaceDataSource(r"D:\IITATE\IITATE_Phase1\arcenv\monitoring" ,
##                                           "SHAPEFILE_WORKSPACE" ,
##                                           Point_lyr_1)

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\AM_"+ str(target_grid) + "_" + path_name,resolution=180)
##    arcpy.mapping.ExportToPDF(mxd,
##                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\MAP_"+ str(target_grid),resolution=180)

del mxd




