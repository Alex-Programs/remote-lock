import httpAPI
import socketAPI
from threading import *
from _vars import _vars

def main():
    _vars.httpAuthorisation = input("HTTP Authorisation Code: ")
    _vars.socketAuthorisation = input("Server Authorisation Code: ")
    Thread(target=socketAPI.run).start()
    httpAPI.run()

if __name__ == "__main__":
    main()