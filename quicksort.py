def part (a,lb,ub):
    i =lb
    j = ub
    piot=a[lb]
    while(i<j):
        while(i<j and a[i]<=piot):
            i=i+1
        while a[j]>piot:
            j=j-1
        if(i>j):
            a[i],a[j] = a[i],a[j]
        a[j]=piot
        return j    
def q_sort(a,lb,ub):
    while(lb<ub):
        part(a,lb,ub)
        pos=part(a,lb,ub)
        q_sort(a,lb,pos-1)
        q_sort(a,pos+1,ub)
print("enter the number of elements in a list")
n=int(input())
a=[]
for i in range(n):
    p=int(input("enter all number "))
    a.append(p)
q_sort(a,0,n-1) 
print(a)           
