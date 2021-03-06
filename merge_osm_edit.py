import re

__author__ = 'coder'
from command_script import apply_changeset_to_db


def replace_osm_with_osmchange(filedata):
    #If the file is already osmChange return.
    if re.search('<osmChange.*?>', filedata):
        return filedata
    m = re.search('<osm.*?>', filedata)
    osm_tag = m.group(0)
    print "OSM tag " + osm_tag
    osm_change_tag = osm_tag.replace("osm", "osmChange")
    print "Change set "+ osm_change_tag
    filedata = filedata.replace(osm_tag, osm_change_tag + "<modify>")
    return filedata


def create_osmchangeset(filein, fileout):
    f = open(filein, 'r')
    filedata = f.read()
    f.close()
    # Create OsmChange file for a submission.
    filedata = filedata.replace("</osm>", "</modify></osmChange>")
    new_data = replace_osm_with_osmchange(filedata)
    f = open(fileout, 'w')
    f.write(new_data)
    f.close()


def process_submission(item):
    # Convert osm -> osmChange and add modify tag
    create_osmchangeset(item, item)
    # Write the changes to database
    apply_changeset_to_db(item)
