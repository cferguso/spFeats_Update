#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Charles.Ferguson
#
# Created:     31/05/2016
# Copyright:   (c) Charles.Ferguson 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def spatFeats(fDir):

    ssa = os.path.basename(fDir)

    spfPoints = fDir + os.sep + ssa + "_p.shp"

    if os.path.exists(spfPoints):
        with arcpy.da.SearchCursor(spfPoints, "*") as rows:
            for row in rows:
                print row

    else:
        print "No point special features file exist for " + ssa





import sys, os, arcpy

inDir = r'D:\Chad\TEMP'
gdb = r'J:\SDJR2016\RO3\R03_FY16.gdb'

dirList = []
for dirpath, dirnames, filenames in os.walk(inDir):
    for dirname in dirnames:
        if dirname[:2].isalpha() and dirname[2:].isdigit():
            dirList.append(dirname)

featTable = gdb + os.sep  + 'featdesc'

for area in dirList:

    featDir = inDir + os.sep + area

    wc = '"AREASYMBOL" = \'' + area.upper() + '\''
    print wc


    with arcpy.da.SearchCursor(featTable, '*', wc) as rows:
        for row in rows:
            print row

    spatFeats(featDir)










