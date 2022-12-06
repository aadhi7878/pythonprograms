import time
time.perf_counter()

s=time.perf_counter()

list=[[23,14,13],[2,6,1],[7,3,86]]
y=[]
for i in list:
    
    y.append(min(i))

print(y)
e=time.perf_counter()
print(e-s)


    
    
    
    

    