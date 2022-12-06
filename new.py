st=input("enter the string")
n=len(st)
i=0
j=0
list=list(st)
fr=int(input("enterr the frame number"))
# print(n)
l=[]
x=n//(fr-1)
rem=n%(fr-1)
while(i<x*(fr-1)):
    for k in range(x):
        l.append(fr)
        for j in range(fr-1):
            l.append(list[i])
            i+=1
l.append(rem)
while(i<n):
    l.append(list[i])
    i+=1



    





