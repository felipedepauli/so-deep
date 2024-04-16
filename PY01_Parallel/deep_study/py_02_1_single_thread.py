import json
import time
from urllib.request import urlopen, Request

def count_letters(url, frequency):
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1

def main():
    frequency = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    
    initial_time = time.perf_counter()
    for i in range(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    final_time = time.perf_counter()
    print(json.dumps(frequency, indent=4))
    evaluate_time = final_time - initial_time
    print(f"Spent time: {evaluate_time*1000:.5} ms")
main()