import eel
from numpy import block

msg = ""


def takeit(text):
    print("Unagas "+text)

@eel.expose
def getText(text):
    takeit(text)

eel.init('web')
eel.start('./templates/index.html', mode='chrome', cmdline_args=['--kiosk'])

