from flask import *
import time

app = Flask(__name__)

class v:
    shouldLock = False

@app.route("/shouldLock")
def checkLock():
    while v.shouldLock == False:
        time.sleep(0.1)

    return "True"

@app.route("/setLock")
def setLock():
    v.shouldLock = True

    #jank
    time.sleep(10)

    v.shouldLock = False
    return ""

@app.route("/")
def index():
    return redirect("https://alexcj.co.uk")
    
app.run(host="0.0.0.0", port=80, threaded=True)