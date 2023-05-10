import socket
host = 'localhost'
port = 8800
if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(5)

    con, addr = socket.accept()
    print('Connect with ', addr)
    con.send('Hello client'.encode('utf-8'))

    data = con.recv(1024)
    print(data.decode('utf-8'))
    data = con.recv(1024)
    arr = data.decode('utf-8')
    a = arr.split(" ")
    res = 0
    x = int(a[1])
    y = int(a[2])
    z = int(a[3])
    if a[0] == '1':
        res = x+y+z
    if a[0] == '2':
        res = x-y-z
    if a[0] == '3':
        res = x*y*z
    if a[0] == '4':
        res = x/y/z
    data = str(res)
    con.send(data.encode('utf-8'))
    con.close()
    socket.close()


