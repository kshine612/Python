#serialize and deserilaize data
import json
emp = {}
emp["empcode"] = input("Enter employee code")
emp["empname"] = input("Enter Employee Name")
emp["date"] = input("Enter date of joining")
emp["salary"] = input("Enter salary")

f = open('sampledata', 'w+')
json.dump(emp,f)
f.seek(0)
inp = json.load(f)
print(inp)

print("End")
f.close()

