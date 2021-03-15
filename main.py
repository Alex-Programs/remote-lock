import requests
import os

host = "localhost:42000"
delay = 5

def lock():
    os.system("loginctl lock-session")

while True:
    time.sleep(delay)
    r = requests.get(host + "/shouldLock")

    if r.text == "True":
        lock()