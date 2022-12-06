


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinked:
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
            self.tail=node
            self.size+=1
    def delete(self,val):
        if(self.head==None):
            print("list is empty")
        elif(self.head.data==val):
            self.head=self.head.next
        
        else:
            cur=self.head
            pre=self.head
            while(cur.next!=None and cur.data!=val):
                pre=cur
                cur=cur.next
            if(cur==None):
                print("element not found")
            else:
                if(cur.next == None):
                    pre.next = cur.next
                    cur = None
                    self.tail = pre
                else:
                    pre.next = cur.next
                    cur = None


    def print(self):
        if(self.head==None):
            print("list is empty")
        else:
            tem=self.head
            while(tem.next!=None):
                print(tem.data,end=" ")
                tem=tem.next
            print(tem.data)
sl=slinked()
sl.insert(1)
sl.insert(23)
sl.insert(26)
sl.insert(29)
sl.insert(19)
sl.insert(100)
sl.print()
sl.delete(100)
sl.delete(29)
sl.delete(23)
sl.insert(122)
sl.print()


        



