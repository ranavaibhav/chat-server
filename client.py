import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostname()
port= 8000

c.connect((host,port))

tm= c.recv(1024)

print("time is %s" % tm.decode('ascii'))

while True:
    a= raw_input('message: ')
    c.send(a)
    b= c.recv(16)
    print "recieved message:",b
    if a == 'end':
        print ('bbye')
        c.close()
        print("time is %s" % tm.decode('ascii'))
        break