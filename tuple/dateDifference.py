#find the number of days difference between two dates
dates = [(4,12,2006),(6,12,2006)]
years=[]
days=[]
months=[]
for el in dates:
    if isinstance(el,tuple):
        years = years+[el[2]]
        months = months+[el[1]]
        days = days+[el[0]]
diff = (years[1]-years[0])*365 + (months[1]-months[0])*30 + (days[1]-days[0])
if diff<0:
    print(diff*-1)
else:
    print(diff)
