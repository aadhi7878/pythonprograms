


def selsort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while(j>=0 and key<list[j]):
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list
l=[1,32,2,4,52,9,16,22]
selsort(l)
print(l)
