from flask import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from _vars import _vars
import socketAPI
import time

print("HTTP API Imported")

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute"]
)

@app.route("/lock")
def lock():
    #FIXME this is for dev purposes
    if _vars.httpAuthorisation == request.headers.get("Authorisation"):
        print("HTTP API has received valid authorisation. Sending to socket API...")
        socketAPI.lock()
        time.sleep(3)
        if _vars.gotResponse:
            _vars.gotResponse = False
            return "200 OK"
        else:
            return "NO RESPONSE"

    else:
        print("Incorrect authorisation received.")
        return "401 Unauthorised"

def run():
    app.run(port=10000, host="0.0.0.0")