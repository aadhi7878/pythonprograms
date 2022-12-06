def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if(list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
                # print(list)
            # else:
                # print(list)
    print("final answer is --->")
    return list          
list=[4,3,2,1]

print(bubblesort(list))    