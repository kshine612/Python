def create_array(a,b,c,n):
    lst=[]
    x =[n]*c
    y = [x]*b
    lst.append([y]*a)
    print(lst)
n=int(input("Ënter number:"))
create_array(2,3,1,n)
