import os

# Open a file
import subprocess
import sys

if len(sys.argv) != 3:
    print "Provide the path to your ogr2osm.py and the root folder to the .shp files"
    exit()

ogr2osm_folder = sys.argv[1]
path = sys.argv[2]


def shp_to_osm(filename):
    cmd = [ogr2osm_folder + "/ogr2osm.py " + filename]
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print "Return code: ", p.returncode
    print out.rstrip(), err.rstrip()


# Recursively goes over dir
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".shp"):
            shp_to_osm(os.path.join(root, file))
