from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

host = ''
port = 8888

def server(host, port):
	sck = socket(AF_INET, SOCK_STREAM)
	sck.bind((host,port))
	sck.listen(1)
	conn, adr = sck.accept()
	print ('Client Connected, IP : ', adr)
	conn.close()

server(host,port)