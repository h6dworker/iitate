#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

Point_measure_shp = r"D:\IITATE_Phase1\Shape\Point_shape\Point_monitoring.shp"
grid_csv = open (r"D:\IITATE_Phase1\csv\GRID.csv",'r')
env.overwriteOutput = True
env.workspace = r"D:\IITATE_Phase1\arcenv\monitoring"

try:
    id = grid_csv.readline()
    while id :
        GRID = id.rstrip('\n')

        out_grid = env.workspace + '\\' + str(GRID) + '.shp'
        where_clause = '"GRID_NAME"='+"'"+str(GRID)+"'"
        arcpy.Select_analysis(Point_measure_shp, out_grid, where_clause)

        GRID_Export = env.workspace + '\\' + str(GRID) + '.shp'

        Kid_Map_count = int(arcpy.GetCount_management(GRID_Export).getOutput(0))
        print str(Kid_Map_count) + " " + GRID_Export

        del out_grid

        id = grid_csv.readline()
        if id == '\n':
            break
finally:
    grid_csv.close()
