with open('abhi.txt','r')as f:
    dt={}
    words=f.read().split()
    for i in words :
        if i not in dt:
            dt[i]=0
        if i in dt:
            dt[i]+=1
    print(dt)
spaces=0    
with open('abhi.txt','r')as f1:
    for i in f1.read():
        if(i==' '):
            spaces+=1
    print(spaces) 
         