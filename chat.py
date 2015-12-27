import socket
import sys
import os

def client(HOST, PORT):
	os.system("clear")
	print """
	   _____ _             _          _           _
  / ____| |           | |        | |         | |
 | (___ | |_ __ _ _ __| |_    ___| |__   __ _| |_
  \___ \| __/ _` | '__| __|  / __| '_ \ / _` | __|
  ____) | || (_| | |  | |_  | (__| | | | (_| | |_
 |_____/ \__\__,_|_|   \__|  \___|_| |_|\__,_|\__|


                                                	"""
	cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cs.connect((HOST, PORT))
	
	while True:
		msg = raw_input('Guest > ')
		cs.send(msg)
		try:
			if msg == '/exit':
				cs.close()
#<<<<<<< HEAD
			data = cs.recv(1024)
			if not data: continue
			print "Host > " + data
#=======
#>>>>>>> b23c3b174833470b0a9cca10b1ca300dbd92a3c9
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
#<<<<<<< HEAD
	print ('Client Connected, IP : ', adr[0])
	while True:
		msg = raw_input('Host > ')
		conn.sendall(msg)
		data = conn.recv(1024)
		if not data: continue
		print "Guest > " + data
		#sck.close()
	conn.close()
#=======
#>>>>>>> b23c3b174833470b0a9cca10b1ca300dbd92a3c9

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