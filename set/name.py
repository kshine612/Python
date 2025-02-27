#add five new names to the set, modify one existing name and delete two names from it
import random
s = set()
while len(s)<5:
    s.add(input("Enter a different name"))
s.discard(input("Enter name to modify:"))
s.pop()
s.pop()
s.add(input("Enter new name:"))
print(s)

    
