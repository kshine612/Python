#enter string and create a dicitonary string the frequency of each letter
s = input("Enter string:")
s=s.lower()
d={}
for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] = d[ch]+1
print(d)
