#if all points lie on same line
x1 = int(input("Enter x1"))
y1 = int(input("Enter y1"))
x2 = int(input("Enter x2"))
y2 = int(input("Enter y2"))
x3 = int(input("Enter x3"))
y3 = int(input("Enter y3"))
m1 = (x2-x1)/(y2-y1)
m2 = (x3-x1)/(y3-y1)
if m1==m2:
    print("They lie on same line")
else:
    print("They don't lie on same line")
