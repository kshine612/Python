#number set
import random
s = set()
while len(s)<10:
    s.add(random.randint(15,45))
c=0
print(s)
for i in s:
    if i<30:
        c=c+1
print("No of integers less than 30:",c)
print(s - {i for i in s if i>35})
