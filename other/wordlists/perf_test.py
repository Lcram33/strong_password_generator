"""
Here are the results that I get, with the EFF's english wordlist (7,776 words) and 1,000 iterations :
RAW : 753.123μs (μs = microseconds, 1μs = 10^-6s)
JSON : 389.534μs

Json is CLEARLY better for performance. Use convert_lists.py to turn your wordlists/quotes lists into json !
"""

your_txt_wordlist_file_here = 'en_wordlist.txt'
your_json_wordlist_file_here = 'wordlist.json'



import json
import time

def convert_time(time_in_ms):
    if time_in_ms > 1000:
        return f"{round(time_in_ms/1000, 3)}s"
    else:
        prefix = ['milli', 'micro', 'nano', 'pico', 'femto', 'atto', 'zepto', 'yocto']
        symbol = ['m', 'μ', 'n', 'p', 'f', 'a', 'z', 'y']

        i = 0
        while time_in_ms < 10**(-3*(i+1)):
            i += 1

        return f"{round(time_in_ms*10**(3*(i+1)), 3)}{symbol[i]}s ({symbol[i]}s = {prefix[i]}seconds)"


def load_wordlist_raw_txt(path):
    wordlist = list()
    with open(path, 'r') as f:
        wordlist = [x.replace('\n', '') for x in f.readlines()]

    return wordlist


def load_wordlist_json(path):
    data = None
    with open(path, 'r') as f:
        data = json.load(f)
    return data


#testing !

iterations = 100
raw_sum = 0
json_sum = 0

for i in range(iterations):
    start = time.time()
    txt_wl = load_wordlist_raw_txt(your_txt_wordlist_file_here)
    print(txt_wl[57])
    end = time.time()
    raw_sum += end - start

    start = time.time()
    json_wl = load_wordlist_json(your_json_wordlist_file_here)
    print(json_wl[57])
    end = time.time()
    json_sum += end - start

print(f"RAW : {convert_time(raw_sum/iterations)} ({raw_sum/iterations}s)")
print(f"JSON : {convert_time(json_sum/iterations)} ({json_sum/iterations}s)")
