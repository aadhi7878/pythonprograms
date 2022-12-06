try:
    with open ("aadhi.txt","r")as f:
        c=0
        l=0
        w=0
        for i in f.readlines():
            l+=1
            w+=len(i.split())
            c+=len(i)
            for k in i:
                if k==" ":
                    c-=1
        print(c,l,w)
except FileNotFoundError as e:
    print(e)