file=open('ad.txt','r')

#print(x,end=" ")
dt={}

for i in file.read().split():
    if i not in dt:
        dt[i]=1
    else:
        dt[i]+=1
print(dt) 




