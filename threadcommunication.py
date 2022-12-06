from threading import *
from time import *
def fun():
    e.set()
    print("green light is on")
    sleep(5)
    print("red light is on")
    e.clear()
def fun1():
    while e.is_set():
        print("you can go.....")
        sleep(.5)
    print("program is done")
e=Event()
t=Thread(target=fun)
t1=Thread(target=fun1)
t.start()
t1.start()