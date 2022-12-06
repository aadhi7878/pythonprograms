import math

n = int(input("enter the no of frames--->"))
frames=[]
frameslength = []
for i in range(n):
	x=input(f"enter the frame {i+1} : ")
	frames.append(x)
	frameslength.append(len(x)+1)
sdata =""
for i in range(n):
	sdata+= str(frameslength[i]) + frames[i]
print(sdata)
received = sdata
z=len(received)
decripcted=""
while(i<z):
    if received[i].isalpha()==False:
        i+=1
    else:
        decripcted+=received[i]
        i+=1
print(decripcted)

