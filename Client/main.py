from socket import *
import time
import os

def main():
    host = "alexcj.co.uk"
    port = 42000
    BufferSize = 2048
    auth = "A"

    targetAddress = (host, port)
    clientSocket = socket(AF_INET, SOCK_STREAM)

    print("Setup socket")

    clientSocket.connect(targetAddress)

    print("Connection halfway")

    message = clientSocket.recv(BufferSize).decode("ascii")

    if message == "PROVIDE AUTHORISATION":
        clientSocket.send(bytes(auth, "ascii"))
        print("Connection complete")

    while True:
        message = clientSocket.recv(BufferSize).decode("ascii")
        print("Received msg")
        if message == "LOCK IMMEDIATELY":
            clientSocket.send(bytes("Acknowledged", "ascii"))
            print("Locking")
            os.system("loginctl lock-session")

        #so if shit breaks it doesn't use too much CPU
        time.sleep(1)
main()
