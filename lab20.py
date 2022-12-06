class stack:
    def __init__(self):
        self.list=[]
        self.size=0
    
    def push_e(self,data):
        self.list.append(data)
    def pop(self):
        self.size-=1
        self.list.pop()
    def peek(self):
        return self.list[-1]
    def print(self):
        print(self.list)
s=stack()
for i in range (0,5):
    s.push_e(i+2)
s.print()
s.pop()
s.print()
print(s.peek())
s.print()