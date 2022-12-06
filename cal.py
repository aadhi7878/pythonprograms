from tkinter import *
root=Tk()
root.geometry("250x343")
Label(root,text="simple calcualtor",fg="black",font="helvatika 15 bold").pack()
f1=Frame(root,height=3)
t=Text(f1,height=3,width=3,font="helvatika 14 bold",bg="green")
t.pack(fill=X)
f2=Frame(root)


f1.pack(fill=X)
f2.pack()
def clear():
    t.delete("1.0","end-1c")
def delete():
    t.delete("end-2c","end-1c")
def modulus():
    t.insert(END,'%')
def devide():
    t.insert(END,'/')
def seven():
    t.insert(END,'7')
def eight():
    t.insert(END,'8')
def nine():
    t.insert(END,'9')
def mul():
    t.insert(END,'*')
def four():
    t.insert(END,'4')
def five():
    t.insert(END,'5')
def six():
    t.insert(END,'6')
def minus():
    t.insert(END,'-')
def one():
    t.insert(END,'1')
def two():
    t.insert(END,'2')
def three():
    t.insert(END,'3')
def plus():
    t.insert(END,'+')
def equalsto():
    exp=t.get("1.0","end-1c")
    x=eval(exp)
    t.insert(END,'=')
    t.insert(END,x)

def zero():
    t.insert(END,'0')
b1=Button(f2,text="clr",font="helvatika 10 bold",height=2,width=6,command=clear)
b2=Button(f2,text="Del",font="helvatika 10 bold",height=2,width=6,command=delete)
b3=Button(f2,text="%",font="helvatika 10 bold",height=2,width=6,command=modulus)
b4=Button(f2,text="/",font="helvatika 10 bold",height=2,width=6,command=devide)
b5=Button(f2,text="7",font="helvatika 10 bold",height=2,width=6,command=seven)
b6=Button(f2,text="8",font="helvatika 10 bold",height=2,width=6,command=eight)
b7=Button(f2,text="9",font="helvatika 10 bold",height=2,width=6,command=nine)
b8=Button(f2,text="*",font="helvatika 10 bold",height=2,width=6,command=mul)
b9=Button(f2,text="4",font="helvatika 10 bold",height=2,width=6,command=four)
b10=Button(f2,text="5",font="helvatika 10 bold",height=2,width=6,command=five)
b11=Button(f2,text="6",font="helvatika 10 bold",height=2,width=6,command=six)
b12=Button(f2,text="-",font="helvatika 10 bold",height=2,width=6,command=minus)
b13=Button(f2,text="1",font="helvatika 10 bold",height=2,width=6,command=one)
b14=Button(f2,text="2",font="helvatika 10 bold",height=2,width=6,command=two)
b15=Button(f2,text="3",font="helvatika 10 bold",height=2,width=6,command=three)
b16=Button(f2,text="+",font="helvatika 10 bold",height=2,width=6,command=plus)
b17=Button(f2,text="=",font="helvatika 10 bold",height=2,width=6,command=equalsto)
b18=Button(f2,text="0",font="helvatika 10 bold",height=2,width=6,command=zero)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=0,column=3)
b5.grid(row=1,column=0)
b6.grid(row=1,column=1)
b7.grid(row=1,column=2)
b8.grid(row=1,column=3)
b9.grid(row=2,column=0)
b10.grid(row=2,column=1)
b11.grid(row=2,column=2)
b12.grid(row=2,column=3)
b13.grid(row=3,column=0)
b14.grid(row=3,column=1)
b15.grid(row=3,column=2)
b16.grid(row=3,column=3)
b17.grid(row=4,column=0)
b18.grid(row=4,column=1)








root.mainloop()