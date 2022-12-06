l=[]
n=int(input("enter the number   "))
for i in range(n):
    l.append(input("enter the number  "))
def bubblesort(l,n):
    for i in range(n-1):
        j=i+1
        for j in range(n):
            if(l[j]<l[j-1]):
                l[j],l[j-1]=l[j-1],l[j]
    return l
print(bubblesort(l,n))