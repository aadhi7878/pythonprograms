print("enter the number of elements in a list")
n=int(input())
a=[]
for i in range(n):
    p=int(input("enter all number "))
    a.append(p)
def l_search(a,key):
    if(a[0]==' '):
        print("list is empty")
    else:
        for i in range(n):
            if(a[i]==key):
                return i
        print("key not found")            
x=int(input("enter a key which you want to search"))
k=l_search(a,x)
print("key reterned at index",k)

