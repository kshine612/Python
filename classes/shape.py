class shape:
    def circle(self, r):
        self.r = r
        self.area = 4*3.14*r*r
        self.circum = 2*3.14*r
        print(self.area, self.circum)
    def rectangle(self, l,b):
        self.area = l*b
        self.circum = 2*(l+b)
        print(self.area, self.circum)
    def square(self, s):
        self.area = s**2
        self.circum = 4*s
        print(self.area, self.circum)
s1 =shape()
s1.circle(2)
s1.rectangle(2,5)
s1.square(2)
