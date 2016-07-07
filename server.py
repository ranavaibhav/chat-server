import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port=8888

serversocket.bind((host,port))
serversocket.listen(5)

while True:
	clientsocket, addr = serversocket.accept()
	print ("got a connection from %s" % str(addr))
	currenttime = time.ctime(time.time()) + "\r\n"
	clientsocket.send(currenttime.encode('ascii'))
while True:
	a= raw_input('message: ')
	clientsocket.send(a)
	if a == 'end'
	    break
	    print 'bbye', currenttime = time.ctime(time.time()) + "\r\n"
	clientsocket.close()