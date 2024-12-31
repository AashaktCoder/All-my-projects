import socket

c = socket.socket()

c.connect(("localhost", 9999))

name = input("Enter your name: ")
c.send(bytes(name, "utf-8"))

print(c.recv(1024).decode())

print("Write q to quit")

msg = ""

while msg != "q":
    msg = input("Write Something: ")
    c.send(bytes(msg, "utf-8"))
    c.send(bytes(msg, "utf-8"))
    if msg == "q":
        c.close()