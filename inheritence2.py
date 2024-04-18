class Box:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

class Student:
    def __init__(self,fees):
        self.fees=fees

class Box2(Box,Student):
    def __init__(self,name,roll,marks,fees):
        self.marks=marks
        Box.__init__(self,name,roll)
        Student.__init__(self,fees)



b1=Box2("riya",52,92,58000)
print(b1.name)
print(b1.roll)
print(b1.marks)
print(b1.fees)

