n=int(input("enter the number"))

l=[]

for i in range(n):
    s=[]
    s.append(input("enter the name"))
    s.append(int(input("enter the age")))
    l.append(s)
print(l.sort(key=lambda x:x[1]))
print(l)
