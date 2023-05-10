import socket
host = 'localhost'
port = 8800

if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    while True:
        data = input('Enter 'r' to start!')
        if data == 'r':
            break
    socket.connect((host,port))
    data = socket.recv(1024)
    print(data.decode('utf-8'))
    socket.send('Hello Server'.encode('utf-8'))
    data = input('Enter your array, start with opt, a, b, c: ')
    socket.send(data.encode('utf-8'))
    data = socket.recv(1024)
    print("Result: ", data.decode('utf-8'))
