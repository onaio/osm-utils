import os
import sys

__author__ = 'coder'

if len(sys.argv) != 4:
    print "Provide the path to your ogr2osm.py and the root folder to the .shp files"
    exit()
path = sys.argv[1]
orig_text = sys.argv[2]
new_text = sys.argv[3]
dirs = os.listdir(path)


def replace(filename, orig_text, new_text):
    f = open(filename, 'r')
    filedata = f.read()
    f.close()
    # Create OsmChange file for a submission.
    newdata = filedata.replace(orig_text, new_text)
    f = open(filename, 'w')
    f.write(newdata)
    f.close()


for file in dirs:
    filename = path + file
    replace(filename, orig_text, new_text)
