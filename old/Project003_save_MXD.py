#! C:/Python27/ArcGIS10.1/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env

env.workspace = r"D:\IITATE_Phase1\arcenv"
env.overwriteOutput = True
kid_csv = open (r"D:\IITATE_Phase1\csv\GRID.csv",'r')

mxd = arcpy.mapping.MapDocument(r"D:\IITATE_Phase1\Project_iitate.mxd")
df = arcpy.mapping.ListDataFrames(mxd, wildcard=None)[0]
symbol_measure_lyr_1 = arcpy.mapping.ListLayers(mxd,"Point_STATIONNO", df)[0]

try:
    id = kid_csv.readline()
    while id :

        GRID = id.rstrip('\n')

        # モニタリングのLYR保存、アプライシンボル、アップデート
        MONI_Polygon_lyr_1 = str(GRID)
        symbol_measure_lyr_1.replaceDataSource(r"D:\IITATE_Phase1\arcenv\monitoring" , "SHAPEFILE_WORKSPACE" , MONI_Polygon_lyr_1)
        print(MONI_Polygon_lyr_1) + "...UpdateLayer"

        # mxdに保存
        mxd.saveACopy(env.workspace + '\\' + 'Project_' + str(GRID) + '.mxd')
        print('Project_' + str(GRID) + '.mxd') + "...saveACopy"

        id = kid_csv.readline()
        if id == '\n':
            break

finally:
    kid_csv.close()

del mxd
del df
