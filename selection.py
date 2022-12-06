def sele(list):
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if(list[min]>list[j]):
                min=j
        list[min],list[i]=list[i],list[min]
    return list
list=[3,5,1,6,9,10]
print(sele(list))