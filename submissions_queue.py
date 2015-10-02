from Queue import Queue
import os
from threading import Thread
from merge_osm_edit import process_submission
from push_osm import push_osm_files

__author__ = 'coder'

path = '/Users/onake/Documents/osm'

def worker():
    while True:
        item = q.get()
        #push_osm_files(item)
        process_submission(item)
        q.task_done()


q = Queue()
num_worker_threads = 10

for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

# name = input("Enter the #no of operation 1: Push OSM 2: Pull OSM 3: Add OSM Change")
#
# # Get submissions from source.
# for item in ["/home/coder/ozm/2_1530.osm", "/home/coder/ozm/3_3193.osm"]:
#     q.put(item)
#


#Recursively goes over dir
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".osm"):
         q.put(os.path.join(root, file))

q.join()  # block until all tasks are done
