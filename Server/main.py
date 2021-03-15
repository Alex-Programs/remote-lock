from flask import *

app = Flask(__name__)

class v:
    shouldLock = False

@app.route("/shouldLock")
def checkLock():
    if v.shouldLock == True:
        v.shouldLock = False
        return "True"

    return "False"

@app.route("/setLock")
def setLock():
    v.shouldLock = True
    return ""

@app.route("/")
def index():
    return redirect("https://alexcj.co.uk")
    
app.run(host="0.0.0.0", port=42000)