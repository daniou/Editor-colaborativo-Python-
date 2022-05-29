
# Program to demonstrate
# timer objects in python
  
import threading
def gfg():
    print("GeeksforGeeks\n")
  
timer = threading.Timer(2.0, gfg)
while 1:
    timer.start()
print("Exit\n")
