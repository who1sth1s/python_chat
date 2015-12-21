from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import sys

def client(HOST, PORT):
	cs = socket(AF_INET, SOCK_STREAM)
	cs.connect((HOST, PORT))
	cs.send('Test')
	data = cs.recv(8192)
	cs.close()

def main(self):
	HOST = raw_input("Input server IP: ")
	PORT = raw_input("Input server PORT: ")
	client(HOST, int(PORT))

if __name__ == '__main__':
	sys.exit(main(sys.argv))

#commit