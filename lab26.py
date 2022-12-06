class stack:
    def __init__(self):
        self.stk=[]
        self.size=0
    def push(self,data):
        self.stk.append(data)
        self.size+=1
    def pop(self):
        if(len(self.stk)==0):
            print("stack is empty")
        else:
            self.size-=1
            return self.stk.pop()
    def peek(self):
        if(len(self.stk)==0):
            print("stack is empty")
        else:
            return self.stk[-1]
    def print(self):
        for i in range(0,self.size):
            print(self.stk.pop(),end=" ")
s=stack()
n=int(input("how many strings do you want to type"))
for i in range(0,n):
    s.push(input("enter the string-->"))
s.print()