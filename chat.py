from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import sys

def client(HOST, PORT):
	cs = socket(AF_INET, SOCK_STREAM)
	cs.connect((HOST, PORT))
	#cs.send('Test')
	#data = cs.recv(8192)
	cs.close()

def server(host, port):
	sck = socket(AF_INET, SOCK_STREAM)
	sck.bind((host,port))
	sck.listen(1)
	conn, adr = sck.accept()
	print ('Client Connected, IP11 : ', adr)
	conn.close()

def main(self):
	option = raw_input("(1)Creative chatting room\n(2)Join the chatting room\nInput: ")
	if option == "1":
		HOST = ''
		PORT = input("Input open PORT: ")
		server(HOST, int(PORT))
		
	elif option == "2":
		HOST = raw_input("Input server IP: ")
		PORT = input("Input server PORT: ")
		client(HOST, int(PORT))

if __name__ == '__main__':
	sys.exit(main(sys.argv))
