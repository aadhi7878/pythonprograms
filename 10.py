def bsearch(l,lb,ub,key):
    while(lb<=ub):
        mid=lb+ub//2
        if(l[mid]==key):
            return mid
        else:
            if(l[mid]>key):
                ub=mid-1
            else:
                lb=mid+1
    return -1
l=[]
n=int(input("enter the number   "))
for i in range(n):
    l.append(int(input("enter the number  ")))
key=int(input("enter the key  "))

a=bsearch(l,0,len(l)-1,key)
if a==-1:
    print("element not found")
else:
    print(f"element present at {a}th index")


