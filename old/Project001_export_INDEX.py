#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE_Phase1"
Project_mxd = env.workspace + '\\' + 'Project_INDEX.mxd'
mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]
field_name = "INDEX_NAME"
path_name = "10"

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    target_name = mxd.dataDrivenPages.pageNameField.name

    print(target_name)

    pageID = mxd.dataDrivenPages.getPageIDFromName("PageName")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(field_name)

    Point_lyr_1 = str(target_grid)

    print(Point_lyr_1) + "...UpdateLayer"

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\AM_SM"+ str(target_grid) + "_" + path_name, resolution=100)

del mxd


