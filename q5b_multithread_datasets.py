# q5b_multithread_datasets
"""Q5b: Multithreaded download and concurrent processing of three datasets."""

import threading
import time
import csv
import requests
from io import StringIO
from functools import reduce

DATA_SOURCES = {
    "population": "https://raw.githubusercontent.com/datasets/population/master/data/population.csv",
    "covid": "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv",
    "temp": "https://datahub.io/core/global-temp/r/annual.csv"
}

downloaded = {}
download_lock = threading.Lock()

def download_dataset(name, url):
    print(f"[{name}] Starting download...")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    text = r.text
    with download_lock:
        downloaded[name] = text
    print(f"[{name}] Download complete.")

def process_population(text):
    reader = csv.DictReader(StringIO(text))
    rows = [r for r in reader if r['Year'] == "2020"]
    total = sum(int(float(r['Value'])) for r in rows)
    print("[population] total (2020):", total)
    return total

def process_covid(text):
    reader = csv.DictReader(StringIO(text))
    
    total_new_cases = 0
    for r in reader:
        try:
            v = r.get('new_cases', '') or r.get('new_cases_smoothed', '') or '0'
            total_new_cases += int(float(v))
        except:
            pass
    print("[covid] total new cases (sum):", total_new_cases)
    return total_new_cases

def process_temp(text):
    reader = csv.DictReader(StringIO(text))
    
    temps = []
    for r in reader:
        try:
            if r.get('Mean') is not None:
                temps.append(float(r['Mean']))
            elif r.get('Temperature') is not None:
                temps.append(float(r['Temperature']))
        except:
            pass
    avg_temp = sum(temps)/len(temps) if temps else 0
    print("[temp] average temperature:", avg_temp)
    return avg_temp

def main():
    
    threads = []
    for name, url in DATA_SOURCES.items():
        t = threading.Thread(target=download_dataset, args=(name, url))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print("All downloads complete.")

    
    threads = []
    results = {}
    def wrap(name, func):
        text = downloaded.get(name)
        if text is None:
            print(f"[{name}] no data to process")
            return
        results[name] = func(text)

    t1 = threading.Thread(target=wrap, args=("population", process_population))
    t2 = threading.Thread(target=wrap, args=("covid", process_covid))
    t3 = threading.Thread(target=wrap, args=("temp", process_temp))

    for t in (t1, t2, t3):
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Concurrent processing results:", results)

if __name__ == "__main__":
    main()
