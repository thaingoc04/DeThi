#SERVER
import socket
from time import ctime

# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8801
host = ''

# binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')

con, addr = sock.accept()
print('Connected with ', addr)
con.send('Hello Client'.encode('utf-8'))
while True:
    # Get data from the client
    data = con.recv(1024)
    if data.decode('utf-8')=='Get Time':
        time= ctime()
        con.send(time.encode('utf-8'))
        print('Send Successfully')
        break
    if data == 'Bye':
        print('Exit Chat')
        con.close()
        break
    print(data.decode('utf-8'))
    sock.send(input().encode('utf-8'))
    sock.close()
