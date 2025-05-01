#merge two files alternatively
f1 = open("C:\\Users\\kriss\\OneDrive\\Desktop\\file1.txt","r")
f2 = open("C:\\Users\\kriss\\OneDrive\\Desktop\\file2.txt","r")
f3 = open("C:\\Users\\kriss\\OneDrive\\Desktop\\file3.txt","w")
while True:
    ch1 = f1.readline()
    f3.write(ch1)
    ch2 = f2.readline()
    f3.write(ch2)
    if not ch1 and not ch2:
        break
f1.close()
f2.close()
f3.close()
print("End")
