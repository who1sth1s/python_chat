import socket

host = ''
port = 8888

def server(host, port):
	sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sck.bind((host,port))
	sck.listen(1)
	conn, adr = sck.accept()
	print ('Client Connected, IP : ', adr)
	conn.close()

server(host,port)