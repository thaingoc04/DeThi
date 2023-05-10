import socket
host = 'localhost'
port = 8800
if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host,port))
    socket.listen(5)

    con, addr = socket.accept()
    con.send('Hello Client'.encode('utf-8'))
    data = con.recv(1024)
    print(data.decode('utf-8'))

    data = con.recv(1024)
    my_string = data.decode('utf-8')
    res = my_string[::-1]
    data = str(res)
    con.send(data.encode('utf-8'))
    con.close()
    socket.close()