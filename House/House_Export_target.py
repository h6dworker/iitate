#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env
import sys

Point_measure_shp = r"D:\IITATE\IITATE_Phase1\Shape\House_shape\House_target.shp"
grid_csv = open (r"D:\IITATE\IITATE_Phase1\csv\KNO.csv",'r')
env.overwriteOutput = True
env.workspace = r"D:\IITATE\IITATE_Phase1\arcenv\House_target"

try:
    id = grid_csv.readline()
    while id :
        KNO = id.rstrip('\n')

        out_grid = env.workspace + '\\K_' + KNO + '.shp'
        singleq = u"'"
        where_clause = u"KNO=" + singleq + KNO + singleq
        arcpy.Select_analysis(Point_measure_shp, out_grid, where_clause)

        GRID_Export = env.workspace + '\\K_' + KNO + '.shp'

        Kid_Map_count = int(arcpy.GetCount_management(GRID_Export).getOutput(0))
        print str(Kid_Map_count) + " " + GRID_Export

        del out_grid

        id = grid_csv.readline()
        if id == '\n':
            break
finally:
    grid_csv.close()
