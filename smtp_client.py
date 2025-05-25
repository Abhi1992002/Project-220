import socket
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
s = socket.socket()

class SmtpClient():
    def __init__(self,port = 25) -> None:
        self.port = port

    def connect(self,server_ip="127.0.0.1"):
        s.connect((server_ip, self.port))
        logging.info(f"Connected to smtp server at port {self.port}")

        # Getting initial data from the smtp server
        self._handling_initial_data_from_server()
        self._accept_commonds()

    def _handling_initial_data_from_server(self):
        initial_data = b""

        while not initial_data.endswith(b"\r\n"):
            initial_data = s.recv(1024)

        logging.info(initial_data.decode())


    def _accept_commonds(self):
        print("\nNow you can communicate with the server using smtp commonds, close connection using :q\n")
        while True:
            commond = input()
            if commond == ":q":
                s.close()
                sys.exit()
            else:
                self._sending_commonds(commond)

    def _sending_commonds(self,commond):
        s.send(f"{commond}\r\n".encode())
        logging.info("Commond send..!!")
        self._handling_commond_response()

    def _handling_commond_response(self):
        response= b""
        while not response.endswith(b"\r\n"):
            part_response = s.recv(1024)
            response += part_response
        logging.info(response.decode())


if __name__ == "__main__":
    server = SmtpClient()
    server.connect()
