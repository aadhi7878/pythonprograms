from threading import *
class Mythread:
    def __init__(self,a):
        self.a=a
    def reserve(self,needed):
        print("available seats:",self.a)
        if(self.a>=needed):
            name=current_thread().name
            print(f'{needed}seat is alloted for {name}')
            self.a-=needed
        else:
            print("no seat is avilable for booking")
            
m1=Mythread(1)
# m2=Mythread(1)
t1=Thread(target=m1.reserve,args=(1,),name='choudary')
t2=Thread(target=m1.reserve,args=(1,),name='aditya')

t1.start()
t2.start()

