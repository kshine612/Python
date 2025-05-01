#accept contact details from the user and create a vcard that we can directly store in our mobile
d={}

d["Name"]=input("Enter name:")
d["Address"]=input("Enter address:")
d["Phone number"]=int(input("Enter phone no:"))
d["Email address"]=input("Enter emmail id:")

f = open("C:\\Users\\kriss\\OneDrive\\Desktop\\Data.txt",'w')

f.write(str(d))

print(f.read)
f.close()
