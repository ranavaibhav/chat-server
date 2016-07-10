import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port=8001

serversocket.bind((host,port))
serversocket.listen(5)

clientsocket, addr = serversocket.accept()
print ("got a connection from %s" % str(addr))
currenttime = time.ctime(time.time()) + "\r\n"
clientsocket.send(currenttime.encode('ascii'))

while True:
    b= clientsocket.recv(1600)

    print ('received message:', b.decode())
    
    a= input('message: ')

    clientsocket.send(a.encode())
    
    if a == 'end':
        print ('bbye')
        currenttime = time.ctime(time.time()) + "\r\n"
        clientsocket.close()
        break