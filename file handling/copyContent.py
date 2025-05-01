#copy contents of one file to another
f1 = open("C:\\Users\\kriss\\OneDrive\\Desktop\\source.txt","r")
f2 = open("C:\\Users\\kriss\\OneDrive\\Desktop\\destination.txt","w")
ch = f1.read(1)
while ch!="":
    if ch.islower():
        f2.write(ch.upper())
    else:
        f2.write(ch)
    ch = f1.read(1)
f1.close()
f2.close()
