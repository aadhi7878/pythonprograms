from re import I


class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def peri(self):
        return 2*(self.l+self.b)
    def val(self):
        return self.l,self.b
    def issquare(self):
        if(self.l==self.b):
            return True
        else:
            return False
r=rect(4,7)
print(r.area())
print(r.issquare())
print(r.peri())









