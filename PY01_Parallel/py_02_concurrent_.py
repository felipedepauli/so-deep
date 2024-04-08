import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping for', seconds, "seconds")
    
process = []

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [ executor.submit(do_something, i) for i in range(10)]
    
print("weeeee")
