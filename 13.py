l=[]
n=int(input("enter the number  "))
for i in range(n):
    l.append(int(input("enter the number  ")))
def sele(l,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if l[j]<l[min]:
                min=j
        l[min],l[i]=l[i],l[min]
    return l
sele(l,n)
print(l)