class complexNo:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i
    def add(self, other):
        print("Addition")
        z = complexNo()
        z.r = self.r + other.r
        z.i = self.i + other.i
        return z
    def sub(self, other):
        print("Subtraction")
        z = complexNo()
        z.r = self.r - other.r
        z.i = self.i - other.i
        return z
    def mul(self, other):
        print("Multiplication")
        z = complexNo()
        z.r = (self.r * other.r) - (self.i * other.i)
        z.i = (self.r * other.i) + (self.i * other.r)
        return z
    def div(self, other):
        print("Division")
        z = complexNo()
        denom = other.i**2 + other.r**2
        z.r = ((self.r * other.r) + (self.i * other.i)) / denom
        z.i = ((self.i * other.r)-(self.r * other.i)) / denom
        return z
    def display(self):
        print("Real = ",self.r,"Imaginary = ", self.i)

c1 = complexNo(2,4)
c2 = complexNo(1,3)
c3=c1.add(c2)
c3.display()
c3=c1.sub(c2)
c3.display()
c3=c1.mul(c2)
c3.display()
c3=c1.div(c2)
c3.display()
