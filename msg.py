class program:
    def __init__(self):
        self.name="giri"
        self.age=25
    def update(self):
        self.name="prabhas"
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return 


obj1=program()
obj2=program()
obj2.update()
print(obj1.age)
print(obj2.age)
if obj1.compare(obj2):
    print("they are same")
else:
    print("they are not same")
