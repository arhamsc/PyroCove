import socket

HOST = '192.168.1.2'
PORT = 9090

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sock.bind((IP, PORT))

# while True:
#     data, (ip,port) = sock.recvfrom(1024)
#     print(f"Sender:{ip} and Port: {port}")
#     print(f"Received message:{data}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            conn.sendall(data)