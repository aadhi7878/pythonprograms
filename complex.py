class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,another):
        return round((self.real+another.real),2) ,round((self.imag+another.imag),2)
    def __sub__(self,another):
        return self.real-another.real,self.imag-another.imag
    def __mul__(self,another):
        a=round((self.real*another.real- self.imag*another.imag),2)
        b=round((self.real*another.imag + self.imag*another.real),2)
        return a,b
com1=complex(4.555,5)
com2=complex(-2,1)
print(com1.__add__(com2))
print(com1.__mul__(com2))