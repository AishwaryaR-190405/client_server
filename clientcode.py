import socket
import threading
# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()   # Server IP / hostname
port = 12345                  # Port number

server.bind((host, port))
server.listen(1)

print("Server started...")
print("Waiting for client connection...")

conn, addr = server.accept()
print("Connected to:", addr)

# Receive messages from client
def receive():
    while True:
        try:
            message = conn.recv(1024).decode()
            print("Client:", message)
        except:
            break

# Send messages to client
def send():
    while True:
        message = input()
        conn.send(message.encode())

thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=send)

thread1.start()
thread2.start()
