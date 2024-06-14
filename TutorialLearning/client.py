import socket

# Client setup
client = socket.socket()
client.connect(('localhost', 8080))

name = input('Enter your name: ')
client.send(name.encode('utf-8'))

while True:
    message = input(f'[{name}]: ')
    client.send(message.encode('utf-8'))
