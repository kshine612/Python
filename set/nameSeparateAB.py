#separate sets names beginning with A and B
s = {"Ayansh","Ayush","Ansh","Bhatt","Brea","Bhavya"}
s1 = {i for i in s if i[0]=='A'}
s2 = {i for i in s if i[0]=='B'}
print(s1)
print(s2)
