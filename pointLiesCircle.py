#point lies on circle
r = int(input("Enter radius:"))
a = int(input("Enter a:"))
b = int(input("Enter b:"))
x = int(input("Enter x:"))
y = int(input("Enter y:"))
r1 = ((x-a)**2)+((y-b)**2)
if r==r1:
    print("Point lies on circle")
else:
    print("Point doesn't lies on circle")
