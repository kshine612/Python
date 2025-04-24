class solid:
    def cube(self, s):
        self.s = s
        self.area = 6*s*s
        self.volume = s**3
        print("Area = ",  self.area, "Volume = ",self.volume)
    def cuboid(self, l, b, h):
        self.area = l*b + b*h + l*h
        self.volume = l*b*h
        print("Area = ",  self.area, "Volume = ",self.volume)
s1 = solid()
s1.cube(3)
s2 = solid()
s2.cuboid(1,2,3)
