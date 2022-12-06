import imp
from tkinter import *
root=Tk()
def check(event):
    print('position is at x=%d, y=%d'%(event.x,event.y))
f=Frame(root,height=1000,width=1000)
f.bind('<Double 1>',check)
f.pack()
root.mainloop()