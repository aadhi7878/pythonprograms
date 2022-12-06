def bsearch(list,lb,ub,key):
    if(lb<=ub):
        mid=lb+ub//2
        if (list[mid]==key):
            return mid
        elif(list[mid]>key):
            return bsearch(list,lb,mid-1,key)
        else:
            return bsearch(list,mid+1,ub,key)
    return -1
list=[]
n=int(input("enter the number   "))
for i in range(n):
    list.append(int(input("enter the number  ")))
key=int(input("enter the key  "))

a=bsearch(list,0,len(list)-1,key)
if a==-1:
    print("element not found")
else:
    print(f"element present at {a}th index")

