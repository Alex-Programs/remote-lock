import requests
import os
import time

host = "http://localhost:80"

def lock():
    os.system("loginctl lock-session")

while True:
    time.sleep(2.5)
    r = requests.get(host + "/shouldLock")
    print(r.text)
    if "True" == r.text:
        print("Locking")
        lock()
