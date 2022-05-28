from io import SEEK_SET
import socket 
import threading
import pickle
import os
from Tasks import *
from time import sleep

HEADER = 64
PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

tasks = Tasks()

def writeInFile(path,content,mode):
    #print(f"{path}, {content}, {mode}")
    f = open(path,mode)
    # print(f)
    # f.seek(0)                        ?¿?¿?¿?¿?  WTF, el seek no funciona :(  ?¿?¿?¿?¿?¿?¿?¿? 
    f.write(content)
    f.flush()
    f.close()

def queueTask(task):
    tasks.addTask(task)
    print("Numero de tasks ", tasks.getNumTasks())

def createTask(id, args):
    queueTask(Task(id, args))
    # print(f"EL USUARIO {id} HA CREADO LA TAREA {args} ")

def send(conn, msg):
    message = pickle.dumps(msg)
    msg_length = len(message)
    send_length = pickle.dumps(str(msg_length))
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    # conn.send("Msg received".encode(FORMAT))
    conn.send(message)

def handle_client(conn, addr, id):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = pickle.loads(conn.recv(HEADER))
        # print("EL TAMAÑO DEL MENSAJE RECIBIDO: ",msg_length)
        #print("que cojones esta pasando ",msg_length)
        if int(msg_length) > 0:
            msg_length = int(msg_length)
            msg = pickle.loads(conn.recv(msg_length))
            print("EL MENSAJE RECIBIDO: ",msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "UPDATE":
                # print("ENTRA A UPDATE")
                send(conn,"nudes")
            else:
                # print("ENTRA A createTask")
                createTask(id,msg)
            print(f"[{addr}] {msg}")

    conn.close()



def executeTask():
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",tasks.getNumTasks())
    if(tasks.getNumTasks() >= 1): 
    # Write in File debe también pillar en qué coordenada tiene que escribir.
        if(tasks.getNextTask().getAction()=='w' or tasks.getNextTask().getAction()=='a'):
            #print("LO DE DENTRO DE LA TASK ",tasks.getNextTask().getFile(), tasks.getNextTask().getContent(),tasks.getNextTask().getAction())
            writeInFile("./demo/Archivos/"+tasks.getNextTask().getFile(), tasks.getNextTask().getContent(),tasks.getNextTask().getAction())
        tasks.nextTaskCompleted()

def taskExecution():
    while True:
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        executeTask()
        sleep(0.15)



def start():
    thread = threading.Thread(target=taskExecution)
    thread.start()
    
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    clients = 0
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
        thread.start()
        clients += 1
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()