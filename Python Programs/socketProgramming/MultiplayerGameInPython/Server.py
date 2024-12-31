import socket
from threading import Thread

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(5)

def MakeNewPlayer(c, addr):
    print("Connected with ", addr)
    c.send(bytes(str(c.recv(1024).decode()), "utf-8"))
    while c.recv(1024).decode() != "500":
        print(c.recv(1024).decode())
    c.close()

while True:
    c, addr = s.accept()
    Thread(target=MakeNewPlayer, args=(c, addr)).start()