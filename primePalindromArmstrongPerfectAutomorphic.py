#check whether a number is prime, perfect, armstrong, palindrome and automorphic
def isPrime(n):
    c=0
    for a in range(2,n):
        if n%a==0:
            c=1
    if c==1:
        return False
    else:
        return True
def isPerfect(n):
    sum=0
    for a in range(1,n):
        if n%a==0:
            sum = sum+a
    if sum==n:
        return True
    else:
        return False
def isArmstrong(n):
    sum=0
    num =n
    while num>0:
        a = num%10
        num=num/10
        sum = sum+ int(a*a*a)
    if sum==n:
        return True
    else:
        return False
def isPalindrome(n):
    return str(n)==str(n)[::-1]
def isAutomorphic(n):
    sq = n*n
    if sq%10==n%10:
        return True
    else:
        return False
n = int(input("Enter a number:"))
print("Prime: ",isPrime(n))
print("Perfect:",isPerfect(n))
print("Armstrong:",isArmstrong(n))
print("Palindrome: ",isPalindrome(n))
print("Automorphic:",isAutomorphic(n))
    
        
        
