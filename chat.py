import socket
import sys
import os
import thread

'''class ThreadClass(threading.Thread):
	def serverdata(sck, adr):
		while True:
			data = sck.recv(1024)
			if not data: break
			sck.sendall(data)

		sck.close()'''

def serverdata(sck, adr):
	data = sck.recv(1024)
	#if not data: break
	#sck.sendall(data)
	print data

def serversend(sck, adr):
	msg = raw_input('msg >')
	try:
		if msg == '/exit':
			sck.close()
		sck.send(msg)
	except:
		sck.close()

def clientsend(sck, cs):
	msg = raw_input('msg >')
	try:
		if msg == '/exit':
			sck.close()
		sck.send(msg)
	except:
		sck.close()

def clientdata(sck, cs):
	data = sck.recv(1024)
	#if not data: break
	#sck.sendall(data)
	print data

def client(HOST, PORT):
	os.system("clear")
	cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cs.connect((HOST, PORT))
	
	while True:
		msg = raw_input('msg >')
		try:
			if msg == '/exit':
				cs.close()
			cs.send(msg)

			data = cs.recv(1024)
			if not data: break
			cs.sendall(data)
			print data			
		except:
			cs.close()


def server(host, port):
	os.system("clear")
	print """
	   _____ _             _          _           _
  / ____| |           | |        | |         | |
 | (___ | |_ __ _ _ __| |_    ___| |__   __ _| |_
  \___ \| __/ _` | '__| __|  / __| '_ \ / _` | __|
  ____) | || (_| | |  | |_  | (__| | | | (_| | |_
 |_____/ \__\__,_|_|   \__|  \___|_| |_|\__,_|\__|
                                                	"""
	print "%s"% socket.gethostbyname(socket.gethostname())
	sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sck.bind((host,port))
	sck.listen(1)
	conn, adr = sck.accept()
	
	print ('Client Connected, IP : ', adr)
	
	while True:
		msg = raw_input('msg >')
		try:

			if msg == '/exit':
				conn.close()
			conn.send(msg)

			data = conn.recv(1024)
			if not data: break
			conn.sendall(data)
			print data
		except:
			conn.close()

	'''
	t = ThreadClass()
	t.start(serverdata,(conn,adr))'''

	
	'''while True:
		msg = raw_input('msg >')
		try:
			if msg == '/exit':
				sck.close()
			sck.send(msg)
		except:
			sck.close()
	conn.close()'''

def main(self):
	option = raw_input("(1)Creative chatting room\n(2)Join the chatting room\nInput: ")
	if option == "1":
		HOST = ''
		PORT = input("Input open PORT: ")
		print socket.gethostbyname(socket.gethostname())
		server(HOST, int(PORT))
		
	elif option == "2":
		HOST = raw_input("Input server IP: ")
		PORT = input("Input server PORT: ")
		client(HOST, int(PORT))


if __name__ == '__main__':
	sys.exit(main(sys.argv))