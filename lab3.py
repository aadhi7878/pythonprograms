def count(file):
    try:
        chars=0
        words =0
        lines=0
        with open(file,'r')as f:
            for i in f.readlines():
                lines+=1
                words+=len(i.split())
                chars+=len(i)-1
                for j  in i:
                    if j==" ":
                        chars-=1



        print(lines,words,chars)

    except FileNotFoundError as e:
        print(e)
count('aadhi.txt')