# q5a_threads
"""Threading demo: three threads printing name and numbers 1-5."""

import threading
import time

def worker(name):
    for i in range(1,6):
        print(f"[{name}] {i}")
        time.sleep(1)
    print(f"[{name}] done")

def main():
    threads = []
    for n in range(1,4):
        t = threading.Thread(target=worker, args=(f"Thread-{n}",))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All threads complete.")

if __name__ == "__main__":
    main()
