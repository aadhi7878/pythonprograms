import os
filename=input("enter the file name-->")
name=f'.\{filename}.txt'
if(os.path.isfile(name)):
    with open(name,'r')as f:
        
        data=f.read()
        list=(data.split())
        words=len(list)
        print(words)
        print(len(data))
    with open(name,'r')as f:    
        line=f.readlines()
        print(len(line))
else:
    print("file not exist")


