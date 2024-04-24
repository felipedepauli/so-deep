import json
import time
from urllib.request import urlopen, Request
from threading import Thread, Lock

class CountingThings():
    def __init__(self):
        self.frequency = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        self.mutex = Lock()
        
    def count_letters(self, url, frequency):
        response = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
        txt = str(response.read())
        for l in txt:
            letter = l.lower()
            if letter in frequency:
                self.mutex.acquire()
                frequency[letter] += 1   
                self.mutex.release() 
                
    def run(self):
        
        initial_time = time.perf_counter()
        
        threads = []
        for i in range(1000, 1020):
            t = Thread(target=self.count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", self.frequency))
            t.start()
            threads.append(t)
            
        for t in threads:
            t.join()
            
        final_time = time.perf_counter()
        print(json.dumps(self.frequency, indent=4))
        evaluate_time = final_time - initial_time
        print(f"Spent time: {evaluate_time*1000:.5} ms")
        my_sum = sum(list(self.frequency.values()))
        print("Total sum:", my_sum)

ct = CountingThings()
ct.run()