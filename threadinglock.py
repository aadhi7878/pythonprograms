
from threading import *

class flight:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        self.l=Lock()
    def reserve(self,needed):
        self.l.acquire()
        print(f"available seats {self.availableseats}")
        if(self.availableseats>=needed):
            name=current_thread().name
            print(f"{needed}seats are booked for {name}")
            self.availableseats-=needed
        else:
            print("all seats are booked sorry for the inconvinence")
        self.l.release()
f=flight(2)
t=Thread(target=f.reserve,args=(1,),name='aditya')
t1=Thread(target=f.reserve,args=(1,),name='akill')
t2=Thread(target=f.reserve,args=(1,),name='a')
t.start()
t1.start()
t2.start()
t.join()
t1.join()
t2.join()