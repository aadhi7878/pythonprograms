
import sys

def b_search(a,lb,ub,key):
    if(lb<=ub):
        mid= (lb+ub)//2
        if key == a[mid]: 
            return mid

        elif key < a[mid]:
            b_search(a,lb,mid-1,key)
        else:
            b_search(a,mid+1,ub,key)

    return -1    

n=int(input("enter the number of elements"))
a=[]
for i in range(n):
    p=int(input("enter the number")) 
    a.append(p)
key=int(input("enter the key"))  
key=int(sys.argv[1])  
x=b_search(a,0,n-1,key)

if(x== '-1'):
    print("key not found")
else:
    print(f"key found at {b_search(a,0,n-1,key)}th index")
             
