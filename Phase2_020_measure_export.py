#! C:/Python27/ArcGIS10.3/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"
path_name = "20"
##field_name = "GRID_NAME"
##Project_mxd = env.workspace + '\\' + 'Phase2_20_BM_Measure.mxd'
##field_name = "GRID_NAME"
##Project_mxd = env.workspace + '\\' + 'H26_20_GRID.mxd'

pt = 1

# 拡張版
##field_name = "GRID_LARGE"
##Project_mxd = env.workspace + '\\' + 'Enlarge_Phase2_20_BM_Measure.mxd'
field_name = "GRID_LARGE"
Project_mxd = env.workspace + '\\' + 'Enlarge_H26_20_GRID.mxd'

mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]

Point_st_lyr1 = arcpy.mapping.ListLayers(mxd,"PT1", df)[0]
Point_st_lyr2 = arcpy.mapping.ListLayers(mxd,"PT2", df)[0]
Point_st_lyr3 = arcpy.mapping.ListLayers(mxd,"PT3", df)[0]

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):

    if   pt == 1:
        Point_st_lyr1.visible = True

    elif pt == 2:
        Point_st_lyr2.visible = True

    elif pt == 3:
        Point_st_lyr3.visible = True

    mxd.dataDrivenPages.currentPageID = pageNum
    pageID = mxd.dataDrivenPages.getPageIDFromName("GRID_NAME")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(field_name)

    Point_lyr_1 = str(target_grid)
##    Point_st_lyr.replaceDataSource(r"D:\IITATE\IITATE_Phase1\arcenv\monitoring" ,
##                                           "SHAPEFILE_WORKSPACE" ,
##                                           Point_lyr_1)
##    arcpy.mapping.ExportToPDF(mxd,
##                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\AM_"+ str(target_grid) + "_" + path_name,resolution=180)

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\MAP_"+ str(target_grid),resolution=180)

del mxd




