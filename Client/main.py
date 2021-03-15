import requests
import os
import time

host = "http://alexcj.co.uk:80"

def lock():
    os.system("loginctl lock-session")

while True:
    time.sleep(2.5)
    try:
        r = requests.get(host + "/shouldLock", timeout=60).text
    except requests.exceptions.ReadTimeout:
        r = ""
        pass
    print(r)
    if "True" == r:
        print("Locking")
        lock()
