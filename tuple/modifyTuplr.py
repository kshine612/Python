#modify an element of tuple
tpl = ()
for i in range(5):
    tpl=tpl+tuple((input("Enter a number")))
lst = list(tpl)
num = input("Enter number to be modified")
lst.insert(lst.index(num), (input("Enter number to be added")) )
lst.remove(num)
tpl = tuple(lst)
print(tpl)
