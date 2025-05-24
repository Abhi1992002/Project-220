import socket

s = socket.socket()
print("Socket created successfully")

port = 2045

s.bind(("",port)) # here ip is empty, so it will listen to all the request from all the computer on my server network
print(f"socket binded to {port}")

s.listen(5) # on listening mode with 5 queue size for pending conenction
print("socket is listening")

while True:
    # Establishing connection with the client
    c, addr = s.accept()
    print("get connection from ",addr)

    c.send('Thank you for connecting'.encode())

    c.close()
    break
