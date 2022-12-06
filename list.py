n=50
i=1
while(i<10):
    a=int(input("enter the number"))
    if(a<n):
        print("you entered too small")
        print("you left",(9-i),"choices")
        i+=1
        
        continue
    elif(a==n):
        print("you guessed correctly in ",i,"chances")
        break
    else:
        print("you entered too large") 
        print("you left",(9-i),"choices")
        i+=1  
        
        continue 
print("you completed all the choices ..game over..... you are looser")
        