mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict["email"] = "max@xyz.com"
print(mydict)

if 'lastname' in mydict:
    print(mydict["lastname"])
    
try:
    print(mydict["name"])

except:
    print("Error")

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)