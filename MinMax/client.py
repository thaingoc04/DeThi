import socket

host = 'localhost'
port = 8800
if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))

    data = socket.recv(1024)
    print(data.decode('utf-8'))
    socket.send('Hello Server!'.encode('utf-8'))

    data = input("Enter an array: ")
    socket.send(data.encode('utf-8'))

    data = socket.recv(1024)
    print("Result: ", data.decode('utf-8'))