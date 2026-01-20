import socket

request_socket = socket.socket()

address = "127.0.0.1"
port = 12345

request_socket.connect((address, port))
Flag = True

while Flag:
    data = b""
    while b"\n" not in data:
        data += request_socket.recv(1024)
    print(data.decode())
    data = input("Enter Option: ")
    request_socket.sendall(data.encode() + b"\n")
    
    data = b""
    while b"\n" not in data:
        data += request_socket.recv(1024)
    print(data.decode())
    Flag = False
    

request_socket.close()

#%%
