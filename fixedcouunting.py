s=input("enter the string")
l=list(s)
i=0
fr=int(input("enterr the  frame size"))
ans=""
n=len(s)
x=n//(fr-1)
rem=n%(fr-1)
while(i<x*(fr-1)):
    for k in range(x):
        ans+=str(fr)
        for l in range(fr-1):
            ans+=l[i]
            i+=1
while(i<n):
    ans+=l[i]
    i+=1
print(ans)


