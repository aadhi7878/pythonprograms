i1=int(input("enter the number of rows for matrix 1-->"))
j1=int(input("enter the number of columnsfor matrix 1-->"))
i2=int(input("enter the number of rows for matrix 2-->"))
j2=int(input("enter the number of columns for matrix 2-->"))
m1=[]
for i in range(i1):
    x=[]
    for j in range(j1):
        x.append(int(input("enter the number")))
    m1.append(x)
#print(m1)
m2=[]
for i in range(i2):
    x=[]
    for j in range(j2):
        x.append(int(input("enter the number")))
    m2.append(x)
#print(m2)
# print(m1)
# print(m2)

def evalu(m1,m2):
    if(i1!=i2 or j1!=j2):
        print("we cannot evaluaatae this matrix")
    else:
        result=[]
        for i in range(0,i1):
            x=[]
            for j in range(0,j1):
                y=m1[i][j]+m2[i][j]
                x.append(y)
            result.append(x)
        return result
z=(evalu(m1,m2))
print(z)