import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 12000))
print("Started UDP Server IP Address: 127.0.0.1 and Port: 12000")

while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.decode("utf-8")  
    message = message.upper()

    if rand < 6:
        continue

    print("Received from {}: {}".format(address, message))
    serverSocket.sendto(message.encode("utf-8"), address)

