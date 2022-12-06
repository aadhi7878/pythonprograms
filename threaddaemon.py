from threading import *
from time import *
def fun():
        for i in range(10):
            print("child thread")
            sleep(.2)
t=Thread(target=fun)
t.setDaemon()
t.start()
sleep(1.2)
print("execution completed")