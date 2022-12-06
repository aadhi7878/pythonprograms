import sys
def fun(filename):
    try:
        with open(filename,'r')as f:
            print("file is in read mode")
            dt={}
            for i in f.read().split():
                if i not in dt:
                    dt[i]=1
                else:
                    dt[i]+=1
        print(dt)
    except FileNotFoundError as e:
        print(e)
try:
    fun(sys.argv[1])
except TypeError as e:
    print(e)

