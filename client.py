import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostname()
port= 8888

c.connect((host,port))
tm= c.recv(1024)
while True:
	a= raw_input('message: ')
	serversocket.send(a)
	if a == 'end'
	    break
	    print 'bbye'
	    c.close()
print("time is %s" % tm.decode('ascii'))
