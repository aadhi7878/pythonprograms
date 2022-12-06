from ast import Delete


class deque:
    def __init__(self):
        self.dq=[]
    def enquelast(self,data):
        self.dq.append(data)
    def enquefirst(self,data):
        if(len(self.dq)==0):
            self.dq.append(data)
        else:
            self.dq.insert(0,data)
    def dequelast(self):
        if(len(self.dq)==1):
            print("deleted element is",self.dq[0])
            del(self.dq[0])
        else:
            print("deleted element is",self.dq[-1])
            del(self.dq[-1])
    def dequefirst(self):
        if(len(self.dq)==1):
            print("deleted element is",self.dq[0])
            del(self.dq[0])
        else:
            print("deleted element is",self.dq[0])
            del(self.dq[0])
    def print(self):
        print(self.dq)
d=deque()
d.enquelast(1)
d.enquelast(4)
d.enquelast(12)
d.enquelast(54)
d.enquefirst(101)
d.enquefirst(100)
d.print()
d.dequefirst()
d.dequelast()
d.print()

        
