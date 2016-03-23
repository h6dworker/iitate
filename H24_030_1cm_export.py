#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"

Project_mxd = env.workspace + '\\' + 'H24_30_AM_1cm.mxd'
path_name = "30"

mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]
field_name = "GRID_NAME"
Select_Grid_shp = r"D:\IITATE\IITATE_Phase1\Shape\Point_shape\survey_point.shp"

Point_1cm_lyr = arcpy.mapping.ListLayers(mxd,"Point_1cm", df)[0]
Point_1cm_lyr.visible = True

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("GRID_NAME")

    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(field_name)

    Point_lyr_1 = str(target_grid)
##    Point_1cm_lyr.replaceDataSource(r"D:IITATE\IITATE_Phase1\arcenv\monitoring" ,
##                                           "SHAPEFILE_WORKSPACE" ,
##                                           Point_lyr_1)

    # where_clause = '"GRID_NAME"='+"'" + str(target_grid)+"'"
    # where_clause = '"GRID_NAME"='+"'" + target_grid +"'"
    # where_clause = """ "GRID_NAME"='L6' """
    # where_clause = field_name + """ ='L6' """
    # where_clause = ''' "GRID_NAME" = 'L6' '''
    # where_clause = ' "GRID_NAME" = ' + str(target_grid)
    where_clause = '"' + field_name + '" = ' + "'" + str(target_grid) + "'"
    print where_clause

    arcpy.MakeFeatureLayer_management(Select_Grid_shp , 'Temp_Grid_lyr', where_clause)
    print(Point_lyr_1) + "...UpdateLayer"

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\AM_"+ str(target_grid) + "_" + path_name,resolution=180)

    arcpy.DeleteFeatures_management('Temp_Grid_lyr')

del mxd




