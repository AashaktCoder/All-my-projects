import socket
from time import sleep

c = socket.socket()

c.connect(("localhost", 9999))

n = input("Enter your name: ")
c.send(bytes(n, "utf-8"))

print(c.recv(1024).decode())

sleep(5)