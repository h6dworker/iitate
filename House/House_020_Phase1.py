#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"

path_name = "20"
Project_mxd = env.workspace + '\\' + 'House_' +  path_name + '_Phase1_H24.mxd'

mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]

if path_name == "20":
    Point_station_lyr = arcpy.mapping.ListLayers(mxd,"STATIONNO", df)[0]

elif path_name == "30":
    Point_station_lyr = arcpy.mapping.ListLayers(mxd,"1cm", df)[0]

elif path_name == "50":
    Point_station_lyr = arcpy.mapping.ListLayers(mxd,"1m", df)[0]

else:# path_name == "70"
    Point_station_lyr = arcpy.mapping.ListLayers(mxd,"GM", df)[0]

field_name = "管理番号"
select_name = "KNO"

# Point_station_lyr.visible = True

target_lyr = arcpy.mapping.ListLayers(mxd,"HOUSE_target", df)[0]
building_lyr = arcpy.mapping.ListLayers(mxd,"Building_target", df)[0]

target_lyr.visible = True
building_lyr.visible = True

for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("管理番号")
    print(pageNum)

    row = mxd.dataDrivenPages.pageRow
    target_grid = row.getValue(select_name)
    target_house = row.getValue(field_name)

    Point_lyr_1 = "K_" + str(int(target_grid))
    Point_station_lyr.replaceDataSource(r"D:\IITATE\IITATE_Phase1\arcenv\house_monitoring" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

    target_lyr.replaceDataSource(r"D:\IITATE\IITATE_Phase1\arcenv\House_target" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

    building_lyr.replaceDataSource(r"D:\IITATE\IITATE_Phase1\arcenv\House_building_target" ,
                                           "SHAPEFILE_WORKSPACE" ,
                                           Point_lyr_1)
    print(Point_lyr_1) + "...UpdateLayer"

##    arcpy.SelectLayerByAttribute_management(Point_station_lyr,
##                 "NEW_SELECTION", 'select_name =' + "'" + row.getValue(field_name) + "'")

    arcpy.mapping.ExportToPDF(mxd,
                 env.workspace + '\\' +"EXPORTJPEG\HOUSE\\" + path_name +
                  "\AM_"+ target_house + "_" + path_name,resolution=200)

del mxd


