list=[]
n=int(input("enter the number of students"))
for i in range(n):
    i=[]
    name=input("enter the name  ")
    age=int(input("enter the age "))
    list.append(name)
    list.append(age)
def takeage(age):
    return age[1]
print(list)
print(list.sort(key=takeage))