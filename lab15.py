from contextlib import nullcontext


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
class dlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insert(self,data):
        if(self.head==None):
            node=Node(data)
            self.head=node
            self.tail=node
            self.size+=1
        else:
            node=Node(data)
            self.tail.next=node
            node.pre=self.tail
            self.tail=node
    def delete(self,data):
        if(self.head==None):
            print("list is empty")
        elif self.head.data==data:
            self.head=self.head.next
            self.head.pre=None
            
        else:
            cur=self.head
            while(cur.next!=None and cur.data!=data):
                cur=cur.next
            if(cur==None):
                print("element not found")
            else:
                if(cur==self.tail):
                    cur.pre.next=None
                    self.tail=cur.pre
                else:
                    cur.next.pre=cur.pre
                    cur.pre.next=cur.next

                    

    def print(self):
        if(self.head==None):
            print("list is empty")
        else:
            cur=self.head
            while(cur.next!=None):
                print(cur.data,end=" ")
                cur=cur.next
            print(cur.data)
dl=dlinkedlist()
dl.insert(12)
dl.insert(1)
dl.insert(113)
dl.insert(52)
dl.insert(82)
dl.print()
dl.delete(12)
dl.delete(113)
dl.delete(82)
dl.print()