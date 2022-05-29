from sqlite3 import Time
import eel
from numpy import block
import time
from client import *
from Tasks import *


period = 0.5 
lastSend = time.time()
lastPointer = 0
msg = ""

tasks = Tasks()



def addToMsg(pointer,text):
    global msg
    global lastPointer
    global lastSend
    #si el puntero apunta a la siguiente posición no hace falta hacer ningun cambio de cursor
    if pointer == lastPointer+1:
        msg+=text
    #si el cursor ya no incrementa de forma consecutiva entonces añadimos una tarea
    else:
        task = Task([pointer,"w",msg,time.time()])
        tasks.addTask(task)   
        lastPointer = pointer 
    
    if(time.time()-lastSend > period):
        while(tasks.getNumTasks()>0):   
            print(tasks.getNumTasks())
            sendMsg(tasks.getNextTask())
            tasks.nextTaskCompleted()
            msg =""
            lastSend = time.time()
            lastPointer = pointer 
            

@eel.expose
def getText(pointer,text):
    addToMsg(pointer,text)

eel.init('web')
eel.start('./templates/index.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])