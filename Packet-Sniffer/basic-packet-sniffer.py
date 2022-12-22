import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    print(s.recvfrom(65565)) #Receive all the data from the socket and the parameter is the buffer size