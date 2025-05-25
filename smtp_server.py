import socket
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class SMTPServer():
    def __init__(self, port = 25):
        self.port = port
        self.s = None

    def start_smtp_server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # creating a tcp socket
        self.s.bind(("",self.port))
        logging.info(f"Binding my smtp server with port {self.port}")

        self.s.listen(128)
        logging.info("SMTP server is on listening mode right now")

        self._start_accepting_connections()

    # Here we are accepting the commonds on a single thread, will add concurreny to it
    def _start_accepting_connections(self):
        smtp_server = self.s

        if not smtp_server:
            logging.error("SMTP server is not started properly yet, please restart it again")
            sys.exit()

        while True:
            conn, addr = smtp_server.accept()
            logging.info(f"Got a connection from the address : {addr}")

            # opening message for the client connection
            conn.send("220 PROJECT SMTP SERVER IS READY..!!\r\n".encode())

            while True:
                self._handling_user_commonds(conn)


    def _handling_user_commonds(self,conn):
        encoded_user_commond = b""

        while not encoded_user_commond.endswith(b"\r\n"):
            partial_commond = conn.recv(1024)
            encoded_user_commond += partial_commond

        user_commond = encoded_user_commond.decode().strip()
        logging.info(f"\nGot an user command `{user_commond}`")

        user_commond_type = user_commond.split(" ")[0]

        if user_commond_type == "HELO":
            self._handling_helo_commond(user_commond,conn)
        else:
            conn.send("502 Command not implemented\r\n".encode())
            logging.warning(f"Unknown command: {user_commond}")


    def _handling_helo_commond(self,user_commond, conn):
        user_commond_value = user_commond.split(" ")[1].strip()
        conn.send(f"Hey {user_commond_value},pleased to meet you\r\n".encode())
        logging.info("Successfully answered the HELO command\n")


if __name__ == "__main__":
    server = SMTPServer()
    server.start_smtp_server()
