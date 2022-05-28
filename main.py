from sqlite3 import Time
import eel
from numpy import block
import time

from pandas import period_range

period = 0.5 
lastSend = time.time()
msg = ""



def send(msg):
    print(msg)

def addToMsg(text):
    global msg
    msg+=text
    global lastSend 
    if(time.time()-lastSend > period):
        send(msg)
        msg =""
        lastSend = time.time()

@eel.expose
def getText(text):
    addToMsg(text)

eel.init('web')
eel.start('./templates/index.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])