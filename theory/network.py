import socket
import sys

s = None
try:
    # socket.AF_INET - means we are using ipv4 addreses for this network
    # socket.SOCK_STREAM - we are using TCP
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()

if s:
    s.connect((host_ip,port))
    print ("the socket has successfully connected to google")
else:
    print ("the socket has failed to connect to google")
