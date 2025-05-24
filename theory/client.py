import socket

s = socket.socket()

port = 2045 # i will connect to this port

s.connect(("127.0.0.1",port))

full_data = b""
while True:
    part = s.recv(1024)
    if not part:
        break
    full_data += part

print(full_data.decode())

s.close()
