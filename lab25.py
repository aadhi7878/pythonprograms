n=int(input("enter the number"))
def fubonachi(n):
    if n>=0:
        if n==0 or n==1:
            return n
        else:
            return fubonachi(n-1)+fubonachi(n-2)
    else:
        print("enter integers only")
for i in range(0,n):
    print(fubonachi(i),end=" ")
