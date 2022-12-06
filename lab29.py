import sys
try:
    try:
        with open(sys.argv[1],'r')as f:
            print("file read done successfully")
    except:
        print("give correct file name inorder to read ")
        exit()
    with open(sys.argv[1],'r')as f:
        f.seek(int(sys.argv[2]))
        print(f.read())
except:
    print("please check your file input location make sure that is correct")
    
    