n=int(input("enter the number how many numbers do you want to check"))
l=[]
for i in range (0,n):
    x=int(input("enter the number"))
    l.append(x)
def fun(n):
    x=n
    y=n//2
    z=n//3
    return x+(2*y)+(2*z)
for i in range(0,n):
    print(fun(l[i]))

