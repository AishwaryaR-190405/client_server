import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()   # Same host as server
port = 12345

client.connect((host, port))

print("Connected to server!")

# Receive messages from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print("Server:", message)
        except:
            break
# Send messages to server
def send():
    while True:
        message = input()
        client.send(message.encode())


thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=send)

thread1.start()
thread2.start()