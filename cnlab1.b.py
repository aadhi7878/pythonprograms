


s=input("enter the string  ")
# n=len(s)
i=0
# count=0
while(i<=len(s)-1):
    
    
    if(i<len(s)-1 and s[i]==s[i+1]):
        count=2
        i+=1
        while(s[i]==s[i+1]):
            count+=1
            i+=1
        if count>=5:
            print("$",end="")
            if(count<10):
                print("0",end="")
            print(count,end="")
            print(s[i],end="")
            
        
        else:
            for j in range(count):
                print(s[i],end="")
        i+=1    
    else:
        print(s[i],end="")
        i+=1

# s=input("enter the string")
# for s[i] in range (s):
#     print(s[i],end="")





