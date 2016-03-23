#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE_Phase1"
Project_mxd = env.workspace + '\\' + 'House_20_AM_Measure.mxd'
mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]
field_name = "管理番号"
select_name = "画地NO"

path_name = "20"

Point_station_lyr = arcpy.mapping.ListLayers(mxd,"モニタリング地点", df)[0]
target_lyr = arcpy.mapping.ListLayers(mxd,"HOUSE_target", df)[0]
building_lyr = arcpy.mapping.ListLayers(mxd,"House_building_target", df)[0]
Point_station_lyr.visible = True
target_lyr.visible = True
building_lyr.visible = True

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("管理番号")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(select_name)
    target_house = row.getValue(field_name)

    Point_lyr_1 = "K_" + str(target_grid)
    Point_station_lyr.replaceDataSource(r"D:\IITATE_Phase1\arcenv\house_monitoring" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

    target_lyr.replaceDataSource(r"D:\IITATE_Phase1\arcenv\House_target" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

    building_lyr.replaceDataSource(r"D:\IITATE_Phase1\arcenv\House_building_target" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

    arcpy.mapping.ExportToPDF(mxd,
                 r"D:IITATE\IITATE_Phase1\EXPORTJPEG\HOUSE\\" + path_name +
                  "\AM_"+ target_house.encode('utf-8') + "_" + path_name,resolution=180)

del mxd


