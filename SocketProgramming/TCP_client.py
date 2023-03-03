import socket

echoClient = socket.socket()
echoClient.connect(("127.0.0.1",32007))

while True:
    data = input("Enter the data to send:")
    echoClient.send(data.encode())
    msgRecieved = echoClient.recv(1024)
    print("At client: {0}".format(msgRecieved.decode()))
