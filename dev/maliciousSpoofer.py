from scapy.all import IP, TCP, send

ip = IP(src="189.174.22.222", dst="192.168.1.2")
tcp = TCP(sport=443, dport = 9090, flags = 'S')
data = "Spoof Packet"

pkt = ip/tcp/data

# for i in range(5):
#     send(pkt, count=20)
#     print(f"Packet sent{i+1}")

import socket

HOST = '192.168.1.2'
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hi")
    send(pkt, count=20)
    data = s.recv(1024)

# print(f"Received {data!r}")