from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def dimentions(self):
        pass
    @abstractmethod
    def calarea(self):
        pass
class rectangle(polygon):
    def __init__(self):
        self.length=12
        self.bredth=7
    def dimentions(self):
        return self.length,self.bredth
    def calarea(self):
        return self.length*self.bredth
class square(polygon):
    def __init__(self):
        self.side=5
    def dimentions(self):
        return self.side
    def calarea(self):
        return self.side*self.side
class triagle(polygon):
    def __init__(self) -> None:
        self.base=8
        self.height=5
    def dimentions(self):
        return self.base,self.height
    def calarea(self):
        return 0.5*self.base*self.height
    
r=rectangle()
t=triagle()
s=square()

print(r.dimentions())
print(r.calarea())
print(t.dimentions())
print(t.calarea())
print(s.dimentions())
print(s.calarea())