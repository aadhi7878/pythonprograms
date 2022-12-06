def readlinebyline(file):
    try:
        with open(file,'r')as f:
            list=[]
            for line in f:
                list.append(line.strip("\n"))
            list.sort()
            print(list)
    except FileNotFoundError as e:
        print(e)
try:
    readlinebyline('abhi.txt')
    #print("prameters are correct")
except TypeError as t:
    print("give correct paramerters")



