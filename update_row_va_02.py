#! C:/Python27/ArcGIS10.2/python.exe
# -*- coding: Shift-jis -*-

import arcpy
from arcpy import env
import sys
import os

env.overwriteOutput = True
env.workspace = os.getcwd()

in_point =       r"D:\IITATE\GRID\040_work_H25-1\repair_point_recid_branch1_after_repair.shp"

save_layer_shp = r"D:\IITATE\GRID\040_work_H25-1\survey_point.shp"

# 使用するポイントを日付指定
where_clause = """ "UDTDATE" <= date '2015-12-24 00:00:00' AND "CHECK" =  0 AND "CLASSNAME" <> 'その他' AND "FLAG" =1  """

target_lyr = "target_lyr"
arcpy.MakeFeatureLayer_management(in_point, target_lyr , where_clause)

arcpy.CopyFeatures_management(target_lyr, save_layer_shp)

arcpy.AddField_management(save_layer_shp, "VA_1m_BM", "DOUBLE")
arcpy.AddField_management(save_layer_shp, "VA_1m_AM", "DOUBLE")

rows = arcpy.da.UpdateCursor(save_layer_shp,
                             ["SUBNAME","VA_01", "VA_02", "VA_1m_BM", "VA_1m_AM", "AB_V1", "AB_V2"])
for row in rows:
    if (row[0] == u'1_屋根・屋上' or row[0] == u'2_外壁'):
        print row[1]
        row[3] = row[1]
        row[4] = row[5]
    else:
        print row[2]
        row[3] = row[2]
        row[4] = row[6]
    rows.updateRow(row)

del row
del rows

