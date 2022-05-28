import socket
import pickle

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

conection = socket.socket()

def recived():
    conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conection.connect(192.168.56.1, 1024)
    HEADERSIZE = 10
    new_msg = True
    full_msg = b''
    while True:
        msg = conection.recv(16)
    
        if new_msg:
            # print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        # print(f"full message length: {msglen}")

        full_msg += msg

        # print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            # print("full msg recvd")
            #print(full_msg[HEADERSIZE:])
            
            return pickle.loads(full_msg[HEADERSIZE:])
    

def sendMsg(msg):
    HEADERSIZE = 10

    conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conection.bind((ADDR))
    conection.listen(5)

    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = conection.accept()
        # print(f"Connection from {address} has been established.")
        # d = ["test.txt",'w','10',"bruh\n"]
        # d = ["test.txt",'r','10']
        # d = ["test.txt",'r']
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        # print(msg)
        clientsocket.send(msg)