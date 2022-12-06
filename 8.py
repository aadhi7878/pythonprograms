stck=[]
def fun(exe):
    for i in exe:
        if i.isdigit():
            stck.append(i)
        else:
            a=stck.pop()
            b=stck.pop()
            stck.append(eval(f"{b}{i}{a}"))
    return int(stck.pop())
exe='14+93/*'
print(fun(exe))