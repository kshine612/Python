#create lists seprating roll no, name and age of student
data= [(67,"Krissa",18), (46,"Vruti",18)]
roll=[]
name=[]
age=[]
for el in data:
    if isinstance(el,tuple):
        roll = roll + [el[0]]
        name = name + [el[1]]
        age = age + [el[2]]
print(roll,name,age)
