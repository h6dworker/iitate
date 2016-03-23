#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = r"D:\IITATE_Phase1\Shape"

# Target Grid_Name
grid_csv = open (r"D:\IITATE_Phase1\csv\GRID.csv",'r')

# Grid Shape"グリッド"
# Polygon_Grid_shp = r"D:\IITATE_Phase1\Shape\GRID_target.shp"
# 交差部（再出力）
Polygon_Grid_shp = r"D:\IITATE_Phase1\Shape\Select_Shape.shp"

# Target Shape"測定点"
Point_measure_shp = r"D:\IITATE_Phase1\Shape\Point_shape\Point_monitoring.shp"

try:
    id = grid_csv.readline()

    while id :

        GRID = id.rstrip('\n')

        where_clause = '"GRID_NAME"='+"'" + str(GRID)+"'"

        Select_Grid_shp = env.workspace + '\\' + 'Select_Grid_out.shp'

        arcpy.Select_analysis(Polygon_Grid_shp, Select_Grid_shp, where_clause)

        arcpy.MakeFeatureLayer_management(Select_Grid_shp , 'Select_Grid_lyr')

        arcpy.MakeFeatureLayer_management(Point_measure_shp, 'Point_measure_lyr')

        arcpy.SelectLayerByLocation_management ('Point_measure_lyr' ,"WITHIN_CLEMENTINI" ,'Select_Grid_lyr')

        Measure_Export = r'D:\IITATE_Phase1\arcenv\monitoring' + '\\' + str(GRID) + '.shp'

        arcpy.Select_analysis('Point_measure_lyr', Measure_Export, )

        Map_count = int(arcpy.GetCount_management(Measure_Export).getOutput(0))

        print str(Map_count) + " " + Measure_Export

        id = grid_csv.readline()

        if id == '\n':
            break
finally:
    grid_csv.close()







