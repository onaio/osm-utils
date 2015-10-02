from command_script import push_osm_to_db

__author__ = 'onake'

def push_osm_files(item):
    # Convert osm -> osmChange and add modify tag
    push_osm_to_db(item)