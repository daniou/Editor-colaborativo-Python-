from ast import While
from sqlite3 import Time
from black import schedule_formatting
import eel
from numpy import block
import time
from client import *
from Tasks import *
from threading import Timer
import time


period = 0
lastPointer = 0
tasks = Tasks()
addedTask = False
msg=""



def resetVariables():
    global msg
    global addedTask
    msg=""
    addedTask = False


def sendLoop():
    while True:
        sendTasks()
        sleep(period)
    

def sendTasks():
    while(tasks.getNumTasks()>0):   
        print("NUMERO DE TAREAS A ENVIAR ------------------ ",tasks.getNumTasks())
        print(tasks.getNumTasks())
        sendMsg(tasks.getNextTask().toArray())
        tasks.nextTaskCompleted()
        resetVariables()


@eel.expose
def edit(action,pointer,text):
    global lastPointer
    global addedTask
    global msg
    print("assssmalesqueeeeee---------->",text)

    if(not addedTask):
        task = Task([pointer,"a",text,time.time()])
        tasks.addTask(task) 
        addedTask = True
    else:
        #si el puntero apunta a la siguiente posición no hace falta hacer ningun cambio de cursor
        if pointer == lastPointer+1:
            print("se escribe de forma secuencial",tasks.getNextTask().content)
            tasks.getNextTask().content += text
            
        #si el cursor ya no incrementa de forma consecutiva entonces añadimos una tarea
        else:
            task = Task([pointer,"a",msg,time.time()])
            tasks.addTask(task)   
            tasks.getNextTask().print()


    lastPointer = pointer 

thread = threading.Thread(target=sendLoop)
thread.start()
eel.init('web')
eel.start('./templates/index.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])

