from sqlite3 import Time
import eel
from numpy import block
import time
from client import *
from Tasks import *


period = 2 
lastSend = time.time()
lastPointer = 0
msg = ""

tasks = Tasks()



def addToMsg(pointer,text):
    global msg
    global lastPointer
    global lastSend

    #si el puntero apunta a la siguiente posición no hace falta hacer ningun cambio de cursor
    if pointer == lastPointer+1 and time.time()-lastSend < period:
        print("se escribe de forma secuencial")
        msg+=text
    #si el cursor ya no incrementa de forma consecutiva entonces añadimos una tarea
    else:
        task = Task([pointer,"a",msg,time.time()])
        tasks.addTask(task)   
        tasks.getNextTask().print()
    
    if(time.time()-lastSend > period):
        while(tasks.getNumTasks()>0):   
            print(tasks.getNumTasks())
            sendMsg(tasks.getNextTask().toArray())
            tasks.nextTaskCompleted()
            msg =""
            lastSend = time.time()

    lastPointer = pointer 
            

@eel.expose
def getText(pointer,text):
    addToMsg(pointer,text)

eel.init('web')
eel.start('./templates/index.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])
#eel.mainloop()
