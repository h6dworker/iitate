#! C:/Python27/ArcGIS10.3/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE\IITATE_Phase1"

path_name = "20"
Project_mxd = env.workspace + '\\' + 'H27_House_Measure.mxd'

mxd = arcpy.mapping.MapDocument(Project_mxd)
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]

##Point_station_lyr = arcpy.mapping.ListLayers(mxd,"HOUSE_target_driven_H27", df)[0]
Select_Grid_shp = env.workspace + '\\Shape\House_shape\TargetDriven.shp'

##where_clause = """ "CODE" in('MY087', 'MY074') """
arcpy.MakeFeatureLayer_management(Select_Grid_shp , 'HOUSE_target_driven_H27')

field_name = "CODE"
select_name = "House_管理"

# Point_station_lyr.visible = True

##target_lyr = arcpy.mapping.ListLayers(mxd,"HOUSE_target", df)[0]
##building_lyr = arcpy.mapping.ListLayers(mxd,"Building_target", df)[0]
##target_lyr.visible = True
##building_lyr.visible = True


for pageNum in range(1,mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum

    pageID = mxd.dataDrivenPages.getPageIDFromName("管理番号")
    row = mxd.dataDrivenPages.pageRow
    target_grid  = row.getValue(select_name)
    target_house = row.getValue(field_name)

    print '  %d, %s, %s' %(pageNum, target_grid, target_house)

##    arcpy.SelectLayerByAttribute_management(Point_station_lyr,
##                 "NEW_SELECTION", 'select_name =' + "'" + row.getValue(field_name) + "'")
##    if target_house == 'NB057':

    arcpy.mapping.ExportToJPEG(mxd,
                env.workspace + '\\' +"EXPORTJPEG\HOUSE\\" + path_name +
                "\\"+ target_house + '_' + target_grid ,
                resolution=180,
                world_file=False)

del mxd


