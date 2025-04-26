#remove empty tuples from a list of tuple
lst = [(),(25,26),(32,34,15),(),(),(859,87,96,4),()]
l = []
for i in lst:
    if isinstance(i,tuple):
        if i:
            l.append(i)
print(l)
