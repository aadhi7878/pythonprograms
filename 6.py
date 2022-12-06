class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,another):
        return self.a+another.a , self.b+another.b
    def __sub__(self,another):
        return self.a-another.a , self.b-another.b
    def __mul__(self,another):
        x=round((self.a*another.a- self.b*another.b),2)
        y=round((self.a*another.b + self.b*another.a),2)
        return x,y
    c1=complex(2.1,4.5)
    c2=complex(-2,1)
    print(c1 .__add__(c2))
    print(c1 .__mul__(c2))

