import subprocess

__author__ = 'coder'

PUSH_OSM_FILE_TO_DB = "osmosis --read-xml file=FILENAME --write-apidb host=\"127.0.0.1\" database=\"kilimani\" user=\"postgres\" password=\"postgres\" validateSchemaVersion=no"
PULL_OSM_FILE_FROM_DB = "osmosis --read-apidb host=\"127.0.0.1\" database=\"kilimani\" user=\"postgres\" password=\"postgres\" --write-xml file=\"FILENAME\" validateSchemaVersion=no"
APPLY_CHANGESET_TO_DB = "osmosis --read-xml-change file=FILENAME --write-apidb-change host=\"127.0.0.1\" database=\"kilimani\" user=\"postgres\" password=\"postgres\" validateSchemaVersion=no"


def apply_changeset_to_db(filename):
    cmd_string = APPLY_CHANGESET_TO_DB.replace("FILENAME", filename)
    cmd = [cmd_string]
    execute_command(cmd)


def push_osm_to_db(filename):
    cmd_string = PUSH_OSM_FILE_TO_DB.replace("FILENAME", filename)
    cmd = [cmd_string]
    execute_command(cmd)


def pull_osm_from_db(filename):
    cmd_string = PULL_OSM_FILE_FROM_DB.replace("FILENAME", filename)
    cmd = [cmd_string]
    execute_command(cmd)


def execute_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print "Return code: ", p.returncode
    print out.rstrip(), err.rstrip()
