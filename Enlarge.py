#! C:/Python27/ArcGIS10.3/python.exe
# -*- coding: UTF-8 -*-

import arcpy
from arcpy import env
import sys
import os

env.overwriteOutput = True
env.workspace = os.getcwd()

# 拡張用グリッドターゲット（拡張用GRID_ENLARGE.shpからGRID_NAME取得）
in_driven= r"D:\IITATE\IITATE_Phase1\Shape\Enlarge_shape\Enlarge_GRID_target.shp"




# 拡張用サーベイポイント（拡張対象GRID_NAME取得）
in_point= r"D:\IITATE\GRID\033_work_Phase2_拡張版\point.shp"




in_driven_cp = r"D:\IITATE\GRID\Enlarge\Select_Grid_cp.shp"
arcpy.CopyFeatures_management(in_driven, in_driven_cp)

arcpy.DeleteField_management(in_driven_cp,
                            [
                            "GRID_key",
                            "POINT_X","POINT_Y",
                            "AREA_NAME","BLOCK_CL","BLOCK_RW",
                            "GRID_NAM_1","GRID_LARGE",
                            ])

out_feature = r"D:\IITATE\IITATE_Phase1\Shape\Enlarge_shape\Enlarge_survey_point.shp"

arcpy.SpatialJoin_analysis(in_point, in_driven_cp, out_feature,"#","#","#","INTERSECT")

arcpy.AddField_management(out_feature,"GRID_LARGE","TEXT", "", "", 10)

expression = """!GRID_NAME!+ "-" + str(!NO!)"""
arcpy.CalculateField_management(out_feature, "GRID_LARGE",
                                    expression,
                                    "PYTHON_9.3")

