import socket
LOGIN = "login1"
LOGIN2 = "login2"

HOST = '127.0.1.1'  # The server's hostname or IP address
PORTS = [i for i in range(60000, 65535)]         # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for PORT in PORTS:
        try:
            s.connect((HOST, PORT))
            s.bind((HOST, PORT))
            msg = LOGIN2 + '/'+"HW1"
            s.send(msg.encode())
            s.settimeout(100)
            data = s.recv(50000)
            print('Received', repr(data))
        except: 
            pass
