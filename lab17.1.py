import sys


file=open('aadhi.txt','r')
a=file.read()
print(a)
print("file read done")
# except:
#     print("pleasse give the correct existed file name to read")

file1=open('aa.txt','a')
#try:
    
print(file1.write(a))
print("copied successfullly")
# except:
#     print("please give arguements correctly")
file.close()
file1.close()