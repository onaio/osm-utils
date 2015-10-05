from command_script import set_osm_timestamp, set_osm_fake_version

__author__ = 'onake'

def add_timestamp_and_version(filename):
    set_osm_timestamp(filename)
    set_osm_fake_version(filename)
