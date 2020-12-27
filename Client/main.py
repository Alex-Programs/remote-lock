from socket import *

def main():
    host = "127.0.0.1"
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
            print("I should lock now")
main()
