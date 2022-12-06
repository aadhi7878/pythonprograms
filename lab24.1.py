def isprime(n):
    if(n>2):
        
        for i in range(2,n):
            if n%i==0:
                return False
        return True
n=int(input("enter the element"))

if(n==1):
    print("no primes are there")
elif(n==2):
    print("2")
else:
    for i in range(2,n+1):
        if(i==2):
            print("2",end=" ")
        else:
            if(isprime(i)):
                print(i,end=" ")



        

