import socket 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ("127.0.0.1", 12345)

serverSocket.bind(serverAddress)

serverSocket.listen(5)

print("server is listening on ", serverAddress)

while 1:
    print("waiting for a connection...")
    clientSocket, clientAddress = serverSocket.accept()

    try:
        print("Connection from ", clientAddress)

        data = clientSocket.recv(1024)
        print("Received:", str(data.decode("utf-8")))
       #TODO
        with open("Desired path to copy ", "a") as file:
            file.write(str(data.decode("utf-8")))
            file.write("\n")
            file.close()

    finally:
        clientSocket.close()

