#to convert case
s = input("Enter string")

def l():
    s1 = ""
    for ch in s:
        if ord(ch)<=90 and ord(ch)>=65:
            s1= s1+chr(ord(ch)+32)
        elif ord(ch)<=122 and ord(ch)>=97:
            s1 = s1+chr(ord(ch))
    print(s1)

def u():
    s1 = ""
    for ch in s:
        if ord(ch)<=122 and ord(ch)>=97:
            s1 = s1+chr(ord(ch)-32)
        elif ord(ch)<=90 and ord(ch)>=65:
            s1 = s1+chr(ord(ch))
    print(s1)
    

cond = input("Enter l to covert String to lower case")
if cond=='l':
    l()
elif cond=='u':
    u()
