import json
import time
from threading import Thread
from urllib.request import urlopen, Request

total_counting = 0

def count_letters(i, frequency):
    url = f"https://www.rfc-editor.org/rfc/rfc{i}.txt"
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global total_counting
    total_counting += 1

def main():
    frequency = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    initial_time = time.perf_counter()
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(i, frequency)).start()
    
    while total_counting < 20:
        time.sleep(0.5)
    
    final_time = time.perf_counter()
    evaluate_time = final_time - initial_time
    print(f"Spent time: {evaluate_time*1000:.5} ms")
    
    my_sum = sum(list(frequency.values()))
    print("Total sum:", my_sum)
main()