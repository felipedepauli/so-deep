import time
from threading import Thread

def do_work():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Finished work")
    
do_work()

initial_time = time.perf_counter()
for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
    
for _ in range(5):
    t.join()

finish_time = time.perf_counter()
total_time = finish_time - initial_time

print("Total time:", total_time)
