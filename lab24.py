
def primenumbers(n):
    if(n==1):
        print("no prime number is there")
    elif(n==2):
        print("2")
    else:
        print("2",end=" ")
        for i in range(3,n+1):
            flag=1
            for j in range(2,i//2+1):
                if(i%j==0):
                    flag=0
                    break
                
            if(flag==1):
                print(i,end=" ")
                
               
                    
primenumbers(100)

