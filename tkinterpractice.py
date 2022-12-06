# from cgitb import text
from tkinter import *
root=Tk()
lst=['green','yellow','red','pink','blue','black','brown','white','orange','violet']

s=Scrollbar(root)
l=Listbox(root,height=4)
for i in lst:
    l.insert(END,i)
l.pack(side="left",anchor="nw")

s.pack(side="left",anchor='nw')


l.config(yscrollcommand=s.set)
# l.config(yscrollcommand=)
s.config(command=l.yview)
def fun(Event):
    for i in sorted(lst):
        l.config(text=i)
l.bind('<Button-3>',fun)





root.mainloop()




# from tkinter import *
# root=Tk()
# def fr():
#     x=float(e.get())
#     e.delete(0,END)
#     e.insert(END,(x*(9/5))+32)
# def cl():
#     y=float(e.get())
#     e.delete(0,END)
#     e.insert(END,((5/9)*(y-32)))


# var=StringVar
# e=Entry(root,fg="black",textvariable=var,bg="light blue")

# b1=Button(root,text="IN FAHRONHEIT",fg="black",bg="light blue",command=fr)
# b2=Button(root,text="IN CELSIUS",fg="black",bg="light blue",command=cl)
# e.pack()
# b1.pack(side="top")
# b2.pack(side="top")
# # e.config(Command=b1,var.set())


# root.mainloop()