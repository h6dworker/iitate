#! C:/Python27/ArcGIS10.2/python.exe
# -*- coding: UTF-8 -*-

import arcpy
from arcpy import env
import sys
import os

env.overwriteOutput = True

env.workspace = os.getcwd()
# env.workspace = r"C:\IITATE_Phase1\Shape\work"

# in_pda_point = r"C:\IITATE_Phase1\Shape\PDA_shape\survey_point.shp"


if len(sys.argv) > 1:
    shapefile = sys.argv[1]

    in_pda_point = r"G:\work\飯館村\20140811_再取り込み\repair_kma19_kdc5\repair_kma19_kdc5.shp"
    join_grid_feature = r"D:\IITATE_Phase1\Shape\PDA_GRID.shp"
    out_feature = "grid_survey_point.shp"
    arcpy.SpatialJoin_analysis(in_pda_point, join_grid_feature, out_feature,"#","#","#","WITHIN")

    out_wgj_feature= "grid_wgj_survey_point.shp"
    outCS = arcpy.SpatialReference(4326)
    arcpy.Project_management(out_feature, out_wgj_feature, outCS)

    # フィールド名の調整
    arcpy.AddField_management(out_wgj_feature, "LAT", "DOUBLE")
    arcpy.AddField_management(out_wgj_feature, "LNG", "DOUBLE")
    arcpy.AddXY_management(out_wgj_feature)

    arcpy.CalculateField_management(out_wgj_feature, "LNG",
                                    "!POINT_X!",
                                    "PYTHON_9.3")

    arcpy.CalculateField_management(out_wgj_feature, "LAT",
                                    "!POINT_Y!",
                                    "PYTHON_9.3")

    arcpy.ExportXYv_stats(out_wgj_feature,

                [
                "AREA_NAME","BLOCK_CL","BLOCK_RW",
                "SERIALNO","STATIONNO","BRANCH",
                "KOUKU","CLASSNAME","SUBNAME","CLASSNAME2",
                "TEAM","CO_01","CO_02","CO_03","CO_04","CO_05","CO_06","KION","SHITSUDO",
                "HOTSPOT",
                "VA_01","VA_02","VA_03","VA_04","VA_05",
                "VA_01FLAG","VA_01FLAG2",
                "PHOTO1","PHOTO2","PHOTO3","PHOTO4","PHOTO5","COMMENT","CHECK","NAVISTAT",
                "UDTDATE","UDTTIME",
                "GPSNO","NAINO","ICSNO","GMNO",
                "SLOPE","FOREST","FLAG",
                "LAT","LNG"
                ],

                "COMMA",
                "survey_XY_1.csv",
                "ADD_FIELD_NAMES")

else:
    print 'Please input FILE NAME'




