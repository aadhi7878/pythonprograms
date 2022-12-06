import sys
def filecopy(file,file1):
    
    try:
        with open(file,'r')as f, open(file1,'w')as f1:
            f1.write(f.read())
            print("copied successfully")

    except:
        print("file noot found please check once ")
try:
    filecopy(sys.argv[1],sys.argv[2])
    
except:
    print("check the parameters of input and please correct it")
