import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9999))
s.listen(4)

print("Waiting For Client To Connect")

def MultiClient(c, n):
    c.send(bytes("Welcome to the server made by Aashakt", "utf-8"))
    while c.recv(1024).decode() != "q":
        print(print(n, " typed ", c.recv(1024).decode()))
        if c.recv(1024).decode() == "q":
            print(n, " left the chat")
    c.close()   

while True:
    c, addr = s.accept()
    Cname = c.recv(1024).decode()
    print(Cname, " has entered the chat")
    Thread(target=MultiClient, args=(c, Cname)).start()