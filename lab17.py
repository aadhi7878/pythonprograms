import sys


def copy_one_to_another(file1,file2):
    try:
        with open(file1,'r')as f, open(file2,'w')as f1:
            x=f.read()   
            
            
            f1.write(x)
            print("data copied successfully")
    except :
        print("check the in that you are given and correct it")
print("enter the file name")

copy_one_to_another(sys.argc[1],sys.argv[2])


    
