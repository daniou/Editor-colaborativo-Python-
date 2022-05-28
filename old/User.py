from multiprocessing import Pool, Pipe
from multiprocessing.connection import Connection, PipeConnection

from Tasks import *
from usersocket import *


serverPipe:PipeConnection = -1
taskList = Tasks()

def welcome():
    print("| Bienvenido a MemoryHub |\n")

# def SetUpConnection():
#     setUpConection()

def setUpTasks():
    tarea = Task(["./Archivos/test.txt",'a',"bruh\n"])
    tarea2 = Task(["./Archivos/test.txt",'a',"vamos flying\n"])
    taskList.append(tarea)
    taskList.append(tarea2)
    
    t = taskList.getNextTask()
    sendMsg(["./Archivos/test.txt",'a',"vamos flying\n"])


def update():
    pass
    # file = input("Archivo sobre el que ejecutar la acciรณn: ")
    # action = input("Acción a realizar: ")
    # content = input("Contenido: ")
    # taskList.append(Task(file, action, content))
    
    # if (taskList.getNumTasks() > 0):
    #     currentTask = taskList.getNextTask()

       
    # print(recived())

welcome()
#setUpConnection()
setUpTasks()


while True:
    update()
    