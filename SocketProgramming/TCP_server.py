import socket

echoSocket = socket.socket()
echoSocket.bind(("127.0.0.1",32007))
echoSocket.listen()

while True:
    clientSocket, clientAddress = echoSocket.accept()

    while True:

        data = clientSocket.recv(1024)
        print("At server: {0}".format(data))

        clientSocket.send((data.decode()+'hi').encode())
        
        if(data.decode() == "bye"):
            clientSocket.close()
            break