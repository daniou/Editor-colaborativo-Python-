from pydoc import cli
import socket
import pickle
import threading
import datetime
import time
from time import sleep
from Tasks import *
 
HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = "192.168.56.1"
CLIENT = socket.gethostbyname(socket.gethostname())
SERVER =  "192.168.56.1"
ADDR = (SERVER, PORT)
PERIOD = 10

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def start():
    print("-------[[CLIENTE]]-------")
    print(f"[LISTENING] Client is listening on {CLIENT}")
    thread = threading.Thread(target=listen)
    thread.start()
    
def listen():
    print(f"THREAD listening on {CLIENT}")
    while handle_updates():
        print(datetime.datetime.now())
        sleep(PERIOD)
    client.close()
    print("Se ha cerrado la conexion")

def handle_updates():
    connected = True #hay que mirar como comprobar si hay una conexion activa.
    print("EJECUTANDO HANDLE UPDATES")
    print("CONEXION ",connected)
    print("ENVIADO UPDATE")
    sendMsg("UPDATE")
    
    msg_length = pickle.loads(client.recv(HEADER))
    if msg_length:
        msg_length = int(msg_length)
        msg = pickle.loads(client.recv(msg_length))
        print(f"[NEW MESSAGE] from {ADDR}")
        print(msg)
        if msg == DISCONNECT_MESSAGE:
            connected=False
        elif msg == "------Actualizacion":
            print("He recibido la actualización del UPDATE")
        else:
            print(msg)    

    return connected

    

def sendMsg(msg):
    message = pickle.dumps(msg)
    msg_length = len(message)
    send_length = pickle.dumps(str(msg_length))
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #print(pickle.loads(client.recv(2048)))

start()

#sleep(3)
