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
def fldCheck(ssa, points, lines):

    reqFlds = ["FID", "Shape", "AREASYMBOL", "FEATSYM"]
    reqFlds.sort()

    pFlds = [x.name for x in arcpy.Describe(points).fields]
    pFlds.sort()

    lFlds = [x.name for x in arcpy.Describe(lines).fields]
    lFlds.sort()

    if pFlds and lFlds == reqFlds:
        msg = 'Attribute table clean for ' + ssa

        return True,msg

    else:

        msg = 'Attribute table DIRTY for ' + ssa

        return False, msg







def spatFeats(fDir):

    ssa = os.path.basename(fDir)

    spfPoints = fDir + os.sep + ssa + "_p.shp"

    if os.path.exists(spfPoints):
        with arcpy.da.SearchCursor(spfPoints, "*") as rows:
            for row in rows:
                print row

    else:
        print "No point special features file exist for " + ssa

    del row, rows

    spfLines = fDir + os.sep + ssa + "_l.shp"

    print "\nNow for lines\n"

    if os.path.exists(spfLines):
        with arcpy.da.SearchCursor(spfLines, "*") as rows:
            for row in rows:
                pass
                #print row

    else:
        print "No point special features file exist for " + ssa


#================================================================================


import sys, os, arcpy

ssaFail = []

inDir = r'D:\Chad\TEMP'
gdb = r'J:\SDJR2016\RO3\R03_FY16.gdb'

dirList = []
for dirpath, dirnames, filenames in os.walk(inDir):
    for dirname in dirnames:
        if dirname[:2].isalpha() and dirname[2:].isdigit():
            dirList.append(dirname)

featTable = gdb + os.sep  + 'featdesc'

areaCount = 0
for area in dirList:

    featDir = inDir + os.sep + area

    wc = '"AREASYMBOL" = \'' + area.upper() + '\''
    print wc


    with arcpy.da.SearchCursor(featTable, '*', wc) as rows:
        for row in rows:
            #print row
            pass

    spfPoints = featDir + os.sep + area + "_p.shp"
    spfLines = featDir + os.sep + area + "_p.shp"

    if not os.path.exists(spfPoints):
        print "No Special Feature Points file exists for " + area + " skipping to next..."
        ssaFail
        continue
    elif not os.path.exists(spfLines):
        print "No Special Feature Lines file exists for " + area + " skipping to next..."
        continue

    else:

        fC0, fC1 = fldCheck(area, spfPoints, spfLines)
        if fC0:
            print fC1

        else:
            print fC1
            ssaFail.append(area)
            continue







