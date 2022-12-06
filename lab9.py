from unittest import result


def bsearch(list,lb,ub,key):
    if(ub>=lb):
        mid=(lb+ub)//2
        if(list[mid]==key):
            return mid
        
        elif(list[mid]>key):
            return bsearch(list,lb,mid-1,key)
            
        else:
            return bsearch(list,mid+1,ub,key)
            
    else:
        return -1
list=[]
n=int(input("enter the numbers which do you want store in list"))
for i in range(n):
    number=int(input("enterr the number"))
    list.append(number)
key=int(input("enter the number which do you want tp search"))
result=bsearch(list,0,len(list)-1,key)
if(result!=-1):
    print("element found at",result,"th index")
else:
    print("element not found")