
from tkinter import *
root=Tk()
def fact():
    
    x=t.get("1.0","end-1c")
    k.delete("1.0","end-1c")
    if(int(x)<0):
        k.insert(END,"enter interger values")
    elif(x==0):
        k.insert(END,"1")
    else:
        a=1
        for i in range(1,int(x)+1):
            a=a*i
        k.insert(END,a)
   
    



f1=Frame(root)
f2=Frame(root)

f1.pack(anchor="nw",side="left",padx=15)
f2.pack(anchor="nw",side="left",padx=15)
t=Text(f1,height=2,width=10)
k=Text(f1,height=2,width=10)
t.pack(anchor="nw")
k.pack(anchor="nw")
Button(f1,text="result",height=1,width=3,borderwidth=2,padx=10,pady=10,command=fact).pack(side=LEFT)



root.mainloop()
