from Queue import Queue
from threading import Thread
from merge_osm_edit import process_submission

__author__ = 'coder'


def worker():
    while True:
        item = q.get()
        process_submission(item)
        q.task_done()


q = Queue()
num_worker_threads = 10

for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

# Get submissions from source.
for item in ["/home/coder/ozm/OSMWay26772773.osm", "/home/coder/ozm/OSMWay111610079.osm"]:
    q.put(item)

q.join()  # block until all tasks are done
