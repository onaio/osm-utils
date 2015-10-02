from command_script import pull_osm_from_db

__author__ = 'onake'

def pull_osm_files(item):
    # Convert osm -> osmChange and add modify tag
    pull_osm_from_db(item)