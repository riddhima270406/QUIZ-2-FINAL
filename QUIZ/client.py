import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 5000
nickname = input("Enter your nickname: ")

client.connect((ip, port))

print("Connected!!")

def recieve():
    while True:
        messsage = client.recv(2048).decode("utf-8")
        if messsage == "nickname":
            client.send(nickname.encode("utf-8"))
        else:
            print(messsage)

def write():
    while True:
        message = input("Enter the option you think is right: ")
        client.send(message.encode("utf-8"))

thread1 = Thread(target= recieve)
thread1.start()

thread2 = Thread(target= write)
thread2.start()