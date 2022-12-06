stck=[]
def evalu(expression):
    for i in expression:
        if i.isdigit():
            stck.append(i)
        else:
            a=stck.pop()
            b=stck.pop()
            x=eval(f'{b}{i}{a}')
            stck.append(x)
    return int(stck.pop())
print(evalu('14+93/*'))

