def bsearch(list,key):
    lb=0
    ub=len(list)-1
    while(lb<=ub):   
        mid=(lb+ub)//2
        if(list[mid]==key):
            return mid
        elif(list[mid]>key):
            ub=mid-1
        else:
            lb=mid+1
    return -1
list=[12,23,24,25,46,48,51]
key=int(input("enter the number which do you want to search"))

index=bsearch(list,key)
if(bsearch(list,key)!=-1):
    print("element found at",index,"th index")
else:
    print("element not found")
