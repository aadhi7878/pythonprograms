n=int(input("enter the numbers count :"))
a=[]
for i in range(n):
    p=int(input("enter the number"))
    a.append(p)
def inssort(a,n):
    for i in range(n):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a

print(inssort(a,n))

    