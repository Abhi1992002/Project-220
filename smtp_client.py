import socket
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
s = socket.socket()

port = 25 # i will connect to this port

s.connect(("127.0.0.1",port))

# initial data from the smtp server
initial_data = b""

while not initial_data.endswith(b"\r\n"):
    initial_data = s.recv(1024)

logging.info(initial_data.decode())

logging.info("Sending the HELO command")
s.send("HELO abhimanyu.dev\r\n".encode())

logging.info("Receiving the HELO command response")
helo_response= b""
while not helo_response.endswith(b"\r\n"):
    part_helo_response = s.recv(1024)
    helo_response += part_helo_response
logging.info(helo_response.decode())

s.close()
