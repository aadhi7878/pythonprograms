def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multi(x,y):
    return(x*y)
def div(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice=input("enter choice 1/2/3/4:")
    if choice in ('1','2','3','4'):
        num1=float(input("enter a first num"))
        num2=float(input("enter a second num"))
        if choice==1:
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice==2:
            print(num1,"-",num2,"=",substract(num1,num2))
        elif choice==3:
            print(num1,"*",num2,"=",multi(num1,num2))
        elif choice==4:
            print(num1,"/",num2,"=",duv(num1,num2))
        next=input("for next calculation?(yes/no):")
        if next=="no":
            break
    else:
        print("invalid")