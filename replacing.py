with open('abhi.txt','r')as f:
    data=f.read()
    with open('ad.txt','w')as f1:
        f1.write(data)
        for i in data:
            f1.write(i.replace('choudary','aditya'))
        