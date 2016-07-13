import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostname()
port= 8001

c.connect((host,port))

tm= c.recv(1024)

print("time is %s" % tm.decode('ascii'))

while True:
    a= input('message: ')
    c.send(a.encode())
    b= c.recv(1600)
    print ('recieved message:', b.decode())
    if b.decode() == 'end':
        print ("bbye")
        print("time is %s" % tm.decode('ascii'))
        break
    if a == 'end':
        print('bbye')
c.close()