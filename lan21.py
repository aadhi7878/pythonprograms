class queue:
    def __init__(self):
        self.q=[]
    def isempty(self):
        if len(self.q)==0:
            return True
        else:
            return False
    def enque(self,data):
        self.q.append(data)
    def deque(self):
        if(len(self.q)!=0):
            print("deleted element",self.q[0])
            del(self.q[0])
    def print(self):
        if(len(self.q)!=0):
            print(self.q)
qu=queue()
for i in range(0,5):
    qu.enque(i+5)
qu.print()
qu.deque()
qu.print()

