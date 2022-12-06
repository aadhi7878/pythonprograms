name=input("enter the string-->")
with open('abhi.txt','r')as f:
    for i in f.read().splitlines():
        if name in i:
            print(i)
            
   
