class Date:
    def __init__(self, lst):
        self.d = lst[0]
        self.m = lst[1]
        self.y = lst[2]
    def __eq__(self,other):
        if self.d==other.d and self.m==other.m and self.y==other.y:
            return True
        else:
            return False
date1 = Date([6,12,6])
date2 = Date([6,12,6])
print(date1==date2)
