
from tkinter import *
root=Tk()
root.geometry("500x324")
var=StringVar()
var.set("white")
def fun():
    l.config(text=f"you selected the {var.get()} light",bg=var.get())
    
s=Radiobutton(root,text="stop",font="helvatika 10 bold",variable=var,value="red",command=fun)
s.pack(side="top",padx=15)
r=Radiobutton(root,text="ready",font="helvatika 10 bold",variable=var,value="yellow",command=fun)
r.pack(side="top",padx=15)
g=Radiobutton(root,text="go....",font="helvatika 10 bold",variable=var,value="green",command=fun)
g.pack(side="top",padx=15)
l=Label(root,text="this is only indication for the colour",font="helvatika 14 bold",bg="white")
l.pack(side="top")




root.mainloop()