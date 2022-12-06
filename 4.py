file=input("enter file name")
str=input("enter the string")

try:
    with open(file,"r")as f:
        l=[]
        for i in f.readlines():
            if(str in i):
                l.append(i.strip("\n"))
        print(l)
except FileNotFoundError as e:
    print(e)




