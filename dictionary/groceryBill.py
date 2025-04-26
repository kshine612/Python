#grocery, price and grocery, quantity to find total bill
price = {"Rice":250, "Wheat":200,"Flour":60,"Apple":120,"Banana":30}
quantity = {"Rice":15, "Wheat":10, "Flour":5,"Apple":1}
bill={}
print("Bill")
for k in price:
    if k not in bill:
        if k not in quantity:
            continue
        bill[k] = price[k]*quantity[k]
        print(k,":",bill[k])
