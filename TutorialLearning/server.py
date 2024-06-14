import socket

server = socket.socket()
# conection stabilization
host, port = '192.168.1.4',8080
print(f'server listening on {host}:{port}')


server.bind((host,port))
server.listen()

client = []
#make the server online 
willRun = True
while willRun:
    client , address = server.accept()
    print(f"I got a connection with :{address}")

    reciveClientData = client.recv()

    def sendMessage(message=''):
        message = 'Default message'

        if message != '':
            client.send(message.encode('utf-8'))
    client.close()   
        



