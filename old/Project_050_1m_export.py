#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"
Project_mxd = env.workspace + '\\' + 'Project_50_AM_1m.mxd'
mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]
field_name = "GRID_NAME"


path_name = "50"

Point_VA_1m_lyr = arcpy.mapping.ListLayers(mxd,"Point_VA_1m", df)[0]
Point_VA_1m_lyr.visible = True

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("GRID_NAME")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(field_name)

    Point_lyr_1 = str(target_grid)
    Point_VA_1m_lyr.replaceDataSource(r"D:\IITATE\IITATE_Phase1\arcenv\monitoring" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\\" + path_name + "\AM_"+ str(target_grid) + "_" + path_name,resolution=180)

del mxd


