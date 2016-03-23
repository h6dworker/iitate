#! C:/Python27/ArcGIS10.3/python.exe
# -*- coding: shift-jis -*-

import arcpy
from arcpy import env
env.overwriteOutput = True

def main():
    pass

if __name__ == '__main__':
    main()
    # 対象ポイント
    # in_points = r"D:\IITATE\IITATE_Phase1\Shape\House_shape\TargetPoint.shp"
    in_points = r"D:\IITATE\house\20160215_H27_Vol.044\TargetPoint.shp"
    # 対象画地
    in_land_Section = r"D:\IITATE\IITATE_Phase1\Shape\House.gdb\Land_Section"

    out_points = r"D:\IITATE\IITATE_Phase1\Shape\House.gdb/TargetPoint_MinMum"
    out_land_Section = r"D:\IITATE\IITATE_Phase1\Shape\House.gdb/TargetLand_MinMum"

    arcpy.MinimumBoundingGeometry_management(in_points, out_points,
                            geometry_type="ENVELOPE",
                            group_option="LIST",
                            group_field="CODE",
                            mbg_fields_option="NO_MBG_FIELDS")

    arcpy.MinimumBoundingGeometry_management(in_land_Section, out_land_Section,
                            geometry_type="ENVELOPE",
                            group_option="LIST",
                            group_field="CODE",
                            mbg_fields_option="NO_MBG_FIELDS")

    MergetoAll = r"D:\IITATE\IITATE_Phase1\Shape\House.gdb\MergetoAll"
    MergetoDissolve = r"D:\IITATE\IITATE_Phase1\Shape\House.gdb\MergetoDissolve"

    fieldMappings = arcpy.FieldMappings()
    fieldMappings.addTable(out_points)
    fieldMappings.addTable(out_land_Section)
    for field in fieldMappings.fields:
         if field.name not in [
         "CODE"
         ]:
             fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))

    arcpy.Merge_management([out_points, out_land_Section], MergetoAll , fieldMappings)

    arcpy.Dissolve_management(MergetoAll, MergetoDissolve,
                                dissolve_field="CODE", statistics_fields="",
                                multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")


##    h27_update_table = r"D:\IITATE\update\h27\\" + updatedBASE + ".dbf"
##
##    arcpy.AddJoin_management(MergetoDissolve, "CODE", h27_update_table, "CODE" )

##arcpy.CalculateField_management(MergetoDissolve, "House_管理" , "!管理番号_1!", "PYTHON_9.3")
