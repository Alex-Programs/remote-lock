from socket import *
from _vars import _vars
from threading import *
print("Socket API imported")

def run():
    print("Socket initialisation started.")
    sock = socket(AF_INET, SOCK_STREAM)

    host = ""
    port = 42000

    sock.bind((host, port))

    sock.listen(5)

    print("Socket initialisation complete.")

    newConnectionListener(sock)


def newConnectionListener(sock):
    print("Listening to new connections")

    while True:
        try:
            connection, address = sock.accept()

            print("Accepted connection from " + str(address))

            Thread(target=handleClient, args=(connection, address)).start()
        except:
            print("Error in newConnectionListener")
            continue


def handleClient(connection, address):
    print("Handling client " + str(address))

    connection.send(bytes("PROVIDE AUTHORISATION", "utf8"))

    response = connection.recv(_vars.bufferSize).decode("ascii")

    print("Received auth: " + response)

    if response == _vars.socketAuthorisation:
        print("Response received and confirmed.")
        _vars.clients.append(connection)
    else:
        connection.close()

def asyncSend(client=None):
    try:
        client.send(bytes("LOCK IMMEDIATELY", "ascii"))
        response = client.recv(_vars.bufferSize).decode("ascii")
        if response == "Acknowledged":
            _vars.gotResponse = True
    except:
        print("Error in asyncSend")
        pass

def lock():
    _vars.gotResponse = False
    for client in _vars.clients:
        print("Alerted potential client")
        try:
            # this is stupid.
            Thread(target=asyncSend, kwargs=dict(client=client)).start()
        except:
            pass
