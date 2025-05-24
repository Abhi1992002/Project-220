import socket
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # creating a tcp socket

port = 25

s.bind(("",port))
logging.info(f"Binding my smtp server with port {port}")

s.listen(128)
logging.info("SMTP server is on listening mode right now")


# currently our smtp server, only handles one connection at a time
# maybe in future we could add multiple threads for accepting connection
while True:
    conn, addr = s.accept()
    logging.info(f"Got a connection from the address : {addr}")
    conn.send("220 PROJECT SMTP SERVER IS READY..!!\r\n".encode()) # opening message for the client

    # handling command
    encoded_user_commond = b""

    while not encoded_user_commond.endswith(b"\r\n"):
        partial_commond = conn.recv(1024)
        encoded_user_commond += partial_commond

    user_commond = encoded_user_commond.decode().strip()
    logging.info(f"Got an user command {user_commond}")

    time.sleep(3)

    user_commond_type = user_commond.split(" ")[0]

    if user_commond_type == "HELO":
        user_commond_value = user_commond.split(" ")[1].strip()
        conn.send(f"Hey {user_commond_value},pleased to meet you\r\n".encode())
        logging.info("Successfully answered the HELO command")
