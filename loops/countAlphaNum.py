#count number of alphabets and digits in a given string
def count(s):
    countAlpha=0
    countNum = 0
    for ch in s:
        if (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
            countAlpha = countAlpha+1
        elif (ch>='0' and ch<='9'):
            countNum = countNum+1
    print("Number of alphabets: ",countAlpha)
    print("Number of digits: ",countNum)
s = input("Enter a string")
count(s)
