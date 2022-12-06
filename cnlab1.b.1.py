from itertools import count


s=input("enter te string")
n=len(s)
i=0
while(i<n):
    while(i<n and s[i]!='$'):
        print(s[i],end="")
        i+=1
    if(i!=n):
        if(s[i]=='$'):
            i+=1
            count=s[i]
            i+=1
            count=count+s[i]
            i+=1
            for j in range(int(count)):
               print(s[i],end="")
            i+=1


