from io import SEEK_SET
import socket 
import threading
import pickle
import os
from Tasks import *
from time import sleep
import datetime

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PERIOD = 10

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

#la constructora de task tendra que aceptar la id tambien-----------------------------
def createTask(id, args):
    print("CREANDO TAREA")  
    queueTask(Task(args))
    # print(f"EL USUARIO {id} HA CREADO LA TAREA {args} ")

def sendMsg(conn, msg):
    message = pickle.dumps(msg)
    msg_length = len(message)
    send_length = pickle.dumps(str(msg_length))
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def listen(conn,addr,id):
    
    print(f"THREAD listening on {SERVER}")
    while handle_client(conn,addr,id):
        sleep(PERIOD)
        print(datetime.datetime.now())
    conn.close()
    print("Se ha cerrado la conexion")


def handle_client(conn, addr, id):
    connected = True #hay que mirar como se comprueba la conexion    
    msg_length = pickle.loads(conn.recv(HEADER))
    if msg_length:
        msg_length = int(msg_length)
        msg = pickle.loads(conn.recv(msg_length))
        print(f"[NEW MESSAGE] from {addr}")
        if msg == DISCONNECT_MESSAGE:
            connected=False
        elif msg == "UPDATE":
            print("Envio actualizacion")
            sendMsg(conn,"------Actualizacion")
        else:
            createTask(id,msg)  

    return connected



def executeTask():
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",tasks.getNumTasks())
    if(tasks.getNumTasks() > 0): 
    # Write in File debe también pillar en qué coordenada tiene que escribir.
        if(tasks.getNextTask().getAction()=='w' or tasks.getNextTask().getAction()=='a'):
            #print("LO DE DENTRO DE LA TASK ",tasks.getNextTask().getFile(), tasks.getNextTask().getContent(),tasks.getNextTask().getAction())
            writeInFile("prueba.txt", tasks.getNextTask().getContent(),tasks.getNextTask().getAction())
        tasks.nextTaskCompleted()

def taskExecution():
    while True:
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        executeTask()
        



def start():
    print("-------[[SERVER]]-------")
    thread = threading.Thread(target=taskExecution)
    
    thread.start()
    server.listen()
    
    print(f"[LISTENING] Server is listening on {SERVER}")
    clients = 0
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=listen, args=(conn, addr, clients))
        thread.start()
        clients += 1
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start()