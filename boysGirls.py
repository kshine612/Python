#to find names of girls and boys in tuple
names = ["krissa","heer","vruti",("ansh","harsh","arsh","tathya","darsh")]
boys=0
girls=0
for el in names:
    if isinstance(el,tuple):
        l=len(el)
        boys = boys+ l
    else:
        girls = girls+1
print("No of boys=",boys,"girls=",girls)
