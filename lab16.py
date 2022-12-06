class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class deque_singlelinked:
    def __init__(self):
        self.rear=None
        self.front=None
    def enquelast(self,data):
        if(self.front==None):
            node=Node(data)
            self.front=node
            self.rear=node
        else:
            node=Node(data)
            self.rear.next=node
            self.rear=node
    def enquefirst(self,data):
            if(self.front==None):
                node=Node(data)
                self.front=node
                self.rear=node
            else:
                node=Node(data)
                node.next=self.front
                self.front=node
    def dequefirst(self):
        if(self.front==None):
            print("we cannot delete the element")
        elif(self.front==self.rear):
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
    def dequelast(self):
        if(self.front==None):
            print("we cannot delete from this list")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            cur=self.front
            pre=self.front
            while(cur.next!=None):
                pre=cur
                cur=cur.next
            pre.next=None
            cur=None
    def print(self):
        if(self.front==None):
            print("list is empty")
        else:
            cur=self.front
            while(cur.next!=None):
                print(cur.data,end=" ")
                cur=cur.next
            print(cur.data)        
dq=deque_singlelinked()
dq.enquefirst(1)
dq.enquelast(43)
dq.enquelast(83)
dq.enquelast(23)
dq.enquelast(232)
dq.enquefirst(101)
dq.print()
dq.dequefirst()
dq.dequelast()
dq.print()
