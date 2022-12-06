from genericpath import isfile
import os
print(os.getcwd())
filename=input("enter the name of file:-->")
name=f'./{filename}.txt'
lines=0
if os.path.isfile(name):
    print("file exist")
    l=open(name,'r')
    for i in l.readline():
        lines+=1
        word=i.split()
        print(word)
    #l=open(name,'r')    
    #print(sorted(l.readlines()))
    #print(lines)
else:
    print("file not exist")
