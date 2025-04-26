#find min and max salary in a dept
import operator
data = {(1,12):250000, (1,13):260000, (1,14):255000,(2,36):370000, (2,37):420000, (2,38):389000, (3,67):652000, (3,68):687400,(3,69):690000}
d1=[]
d2=[]
d3=[]
for k,v in data.items():
    print(k[0],k[1],v)
    if k[0]==1:
        d1=d1+[v]
    if k[0]==2:
        d2=d2+[v]
    if k[0]==3:
        d3=d3+[v]
print("Maximum in dep 1",max(d1),"Minimum in dep 1",min(d1))
print("Maximum in dep 2",max(d2),"Minimum in dep 2",min(d2))
print("Maximum in dep 3",max(d3),"Minimum in dep 3",min(d3))
