import subprocess
from submissions_queue import *

__author__ = 'coder'

PUSH_OSM_FILE_TO_DB = 'osmosis --read-xml file=%s --write-apidb host=\'%s\' database=\'%s\' user=\'%s\' password=\'%s\''
PULL_OSM_FILE_FROM_DB = 'osmosis --read-apidb host=\'%s\' database=\'%s\' user=\'%s\' password=\'%s\' --write-xml file=\'%s\''
APPLY_CHANGESET_TO_DB = 'osmosis --read-xml-change file=%s --write-apidb-change host=\'%s\' database=\'%s\' user=\'%s\' password=\'%s\''


def apply_changeset_to_db(filename):
    execute_command([APPLY_CHANGESET_TO_DB%(filename, host, database, user, password)])


def push_osm_to_db(filename):
    execute_command([PUSH_OSM_FILE_TO_DB%(filename, host, database, user, password)])


def pull_osm_from_db(filename):
    execute_command([PULL_OSM_FILE_FROM_DB%(host, database, user, password, filename)])

# Set the OSM creation time to now
def set_osm_timestamp(filename):
    execute_command(["osmconvert %s --timestamp=NOW -o=%s"%(filename, filename)])

# Set version to 1 to prevent errors.
def set_osm_fake_version(filename):
    execute_command(["osmconvert --fake-version %s"%filename])

def execute_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print "Return code: ", p.returncode
    print out.rstrip(), err.rstrip()
    if err.rstrip() == "" :
        return True
    else:
        return False

