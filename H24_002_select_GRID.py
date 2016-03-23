#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = r"D:\IITATE\IITATE_Phase1\Shape"

# Target Grid_Name
grid_csv = open (r"D:\IITATE\IITATE_Phase1\csv\GRID.csv",'r')

# Target Shape"測定点"
Point_measure_shp = r"D:\IITATE\IITATE_Phase1\Shape\Point_shape\survey_point.shp"

try:
    id = grid_csv.readline()

    while id :

        GRID = id.rstrip('\n')

        where_clause = '"GRID_NAME"='+"'" + str(GRID)+"'"

        Select_Grid_shp = env.workspace + '\\' + 'Select_Grid_out.shp'

        Measure_Export = r'D:\IITATE\IITATE_Phase1\arcenv\monitoring' + '\\' + str(GRID) + '.shp'

        arcpy.Select_analysis(Point_measure_shp, Measure_Export, where_clause)

        Map_count = int(arcpy.GetCount_management(Measure_Export).getOutput(0))
        print str(Map_count) + " " + Measure_Export

        id = grid_csv.readline()

        if id == '\n':
            break
finally:
    grid_csv.close()







