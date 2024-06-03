from ipaddress import ip_address
import socket
from tkinter import *
from threading import Thread

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


IP_ADDRESS = '127.0.0.1'
PORT = 8000
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def handleClient(client, client_name):
    global clients
    global BUFFER_SIZE
    global SERVER

    # Sending welcome message
    banner1 = "Welcome, You are now connected to Server!\nClick on Refresh to see all available users.\nSelect the user and click on Connect to start chatting."
    client.send(banner1.encode())

    while True:
        try:
            BUFFER_SIZE = clients[client_name]["file_size"]
            chunk = client.recv(BUFFER_SIZE)
            message = chunk.decode().strip().lower()
            if(message):
                handleMessges(client, message, client_name)
            else:
                removeClient(client_name)
        except:
            pass


def acceptconnections():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(2048).decode().lower()
        clients[client_name] = {
            'clients' : client,
            'address' : addr,
            'connected_with' : "",
            'file_name' : "",
            'file_size ' : 4096
        }
        print(f'Connection established with {client_name} : {addr}')
        
        thread = Thread(target= handleClient, args = (client, client_name))

def setup():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)
    
    print("\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print('\n')

    acceptconnections()
    
def ftp():
    global IP_ADDRESS
    
    authorizer = DummyAuthorizer()
    authorizer.add_user('lftpd', 'lftpd', '.', perm = 'elradfmw')
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    ftp_server = FTPServer((IP_ADDRESS, 21), handler)
    ftp_server.serve_forever()
    
setup_thread = Thread(target = ftp)
setup_thread.start()
        
setup_thread = Thread(target = setup)
setup_thread.start()