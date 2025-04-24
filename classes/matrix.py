class Matrix:
    def __init__(self, lst=[0,0,0,0,0,0,0,0,0]):
        self.l = lst
    def add(self, other):
        m = Matrix()
        m.l = [self.l[i]+other.l[i] for i in range(0,9)]
        return m
    def display(self):
        print(self.l)
m1 = Matrix([0,0,0,1,2,3,4,5,6])
m2 = Matrix([0,0,0,1,2,3,4,5,6])
m3 = m1.add(m2)
m3.display()
