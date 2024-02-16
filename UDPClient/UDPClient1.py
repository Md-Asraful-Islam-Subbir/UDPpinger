import socket
import time

while True:
    print("\nChoose your option to continue")
    print("-------------------------")
    print("1. Enter any key to ping to UDP server")
    print("2. Enter 0 to exit program")
    print("-------------------------\n")

    option = input("Enter your option: ")
    option = int(option)

    if option == 0:
        break
    print("-------------------------")
    print("Starting Ping")
    print("-------------------------\n")

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 12000)
    mysocket.settimeout(2)

    try:
        for i in range(0, 9):
            start = time.time()
            message = 'Ping ' + str(i) + " " + time.ctime(start)
            try:
                sent = mysocket.sendto(message.encode("utf-8"), server_address)
                print("Sent " + message)
                data, server = mysocket.recvfrom(4096)
                received_message = data.decode("utf-8")  # Decode the received bytes to string
                print("Received from server: " + received_message)
                end = time.time()
                elapsed = end - start
                print("Time: " + str(elapsed * 1000) + " Milliseconds\n")
            except socket.timeout:
                print("#" + str(i) + " Requested Time out\n")
    finally:
        print("Finish ping, closing socket")
        mysocket.close()
