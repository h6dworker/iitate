#! C:/Python27/ArcGIS10.2/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"

path_name = "50"
field_name = "GRID_NAME"
Project_mxd = env.workspace + '\\' + 'Vol25_Phase1_H25_1m.mxd'

mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]

Point_st_lyr = arcpy.mapping.ListLayers(mxd,"data_H25_1m", df)[0]
Point_st_lyr.visible = True

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("GRID_NAME")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(field_name)
    Point_lyr_1 = str(target_grid)

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\AM_1M_"+ str(target_grid),resolution=180)

del mxd




