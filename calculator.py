from tkinter import *

root=Tk()
f1=Frame(root)

t=Text(f1)
t.grid(row=5,column=6)
l=Label(f1,text="result:")
def one():
    t.insert(END,"1")
def two():
    t.insert(END,"2")
def three():
    t.insert(END,"3")
def four():
    t.insert(END,"4")
def five():
    t.insert(END,"5")
def six():
    t.insert(END,"6")
def seven():
    t.insert(END,"7")
def eight():
    t.insert(END,"8")
def nine():
    t.insert(END,"9")
def zero():
    t.insert(END,"0")


def add():
    t.insert(END,"+")
def min():
    t.insert(END,"-")
def div():
    t.insert(END,"//")
def mod():
    t.insert(END,"%")

def mul():
    if(t.get(END)!='+'):
        t.insert(END,'*')
            
def show():
    output=t.get(0.0,"end-1c")
    res=eval(output)
    #t.insert(0.0,res)
    l.config(text=res)            
one=Button(f1,text="1",command=one)
two=Button(f1,text="2",command=two)
three=Button(f1,text="3",command=three)
four=Button(f1,text="4",command=four)
five=Button(f1,text="5",command=five)
six=Button(f1,text="6",command=six)
seven=Button(f1,text="7",command=seven)
eight=Button(f1,text="8",command=eight)
nine=Button(f1,text="9",command=nine)
zero=Button(f1,text="0",command=zero)
plus=Button(f1,text="+",command=add)
minus=Button(f1,text="-",command=min)
division=Button(f1,text="/",command=div)
multiplication=Button(f1,text="*",command=mul)
modulus=Button(f1,text="%",command=mod)
show1=Button(f1,text="=",command=show)

one.grid(row=0,column=1)
two.grid(row=0,column=2)
three.grid(row=0,column=3)
four.grid(row=1,column=1)
five.grid(row=1,column=2)
six.grid(row=1,column=3)
seven.grid(row=2,column=1)
eight.grid(row=2,column=2)
nine.grid(row=2,column=3)
zero.grid(row=3,column=2)
plus.grid(row=0,column=4)
minus.grid(row=1,column=4)
division.grid(row=2,column=4)
multiplication.grid(row=3,column=3)
modulus.grid(row=3,column=1)
show1.grid(row=3,column=4)




l.grid(row=6,column=6)

root.mainloop()
