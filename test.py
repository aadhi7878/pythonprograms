from math import gcd, lcm
from operator import truediv
def check(a,b):
    p=lcm(a,b)/gcd(a,b)
    if(p<=3):
        return True
    else:
        return False
list=[]

n=int(input("enter the number"))
for i in range (0,n):
    x=int(input("enter the number"))
    list.append(x)
print(list)

def result(a):
    count=0
    for i in range (1,a+1):
        for j in range(1,a+1):
            if(check(i,j)==True):
                count+=1
    print(count)
    
l=[]
for i in range(0,n):
    z=list[i]
    w=result(z)
    l.append(w)

