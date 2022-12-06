from tkinter import *
root=Tk()
def fun():
    i.delete("1.0","end-1c")
    x=t.get("1.0","end-1c")
    y=k.get("1.0","end-1c")
    if(int(x)<0 or int(y)<0):
        i.insert(END,"please enter integer")
        i.config(bg="red")
    elif int(y)==0:
        i.insert(END,"number cannot devisible by zero")
        i.config(bg="red")
    else:
        i.config(bg="white")
        i.insert(END,round(int(x)/int(y),2))

t=Text(root,height=3,width=15,bg="light blue",fg="blue",font="selvatika 14 bold",borderwidth=4,relief=SUNKEN)
k=Text(root,height=3,width=15,bg="light blue",fg="blue",font="selvatika 14 bold",borderwidth=4,relief=SUNKEN)
t.pack(side="top")
k.pack(side="top")
i=Text(root,height=3,width=15,bg="white")
i.pack(side="top")
Button(root,text="devide",font="helvatica 10 bold",command=fun).pack(side="top")


root.mainloop()