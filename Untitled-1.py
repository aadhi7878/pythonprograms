

n=int(input("enter the numbers count :"))
a=[]
for i in range(n):
    p=int(input("enter the number"))
    a.append(p)
def inssort(a,n):
    for i in range(1,n):
        t=a[i]
        j=i-1
        while(j>=0 and a[j]>t):
            a[j+1]=a[j]
            j-1
    a[j+1]=t
inssort(a,n)
print(a)            
            





    
