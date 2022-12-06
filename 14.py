class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.h=None
        self.t=None
    def inserend(self,data):
        
        if(self.h==None):
            node=Node(data)
            self.h=node
            self.t=node
        else:
            node=Node(data)
            self.t.next=node
            self.t=node
    def delete(self,ele):
        if(self.h==None):
            print("we cannot delete the element")
        elif(self.h.data==ele):
            self.h=self.h.next
        else:
            p=None
            c=self.h
            while(c.next!=None and c.data!=ele):
                p=c
                c=c.next
            if(c==None):
                print("element not found")
            elif(c.next==None):
                p.next=c.next
                c=None
                self.t=p
            else:
                p.next=c.next
                c=None
    def print(self):
        t=self.h
        while(t!=None):
            print(t.data,end=" ")
            t=t.next
s=sll()
s.inserend(1)
s.inserend(2)
s.inserend(3)
s.inserend(4)
s.inserend(15)
s.delete(2)
s.print()

        



            


