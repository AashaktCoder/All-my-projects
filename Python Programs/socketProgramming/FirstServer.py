import socket

s = socket.socket()

s.bind(("localhost", 9999))

s.listen(3)
print("Waiting for connection")

while True:
    c, addr = s.accept()
    n = c.recv(1024).decode()
    print("Client Connected with: ", addr, " Name: ",n)

    c.send(bytes("Hello", "utf-8"))

    c.close()