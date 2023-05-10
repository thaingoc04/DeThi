#CLIENT
import socket

# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8801
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
data = sock.recv(4096)
print(data.decode('utf-8'))
while True:
    if data == 'Bye':
        print('Exit Chat')
        sock.close()
        break
    sock.send(input().encode('utf-8'))
    data = sock.recv(4096)
    print(data.decode('utf-8'))