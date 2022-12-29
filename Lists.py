mylist= ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5,True,"apple", "apple"]
print(mylist2)

item = mylist[-1]
print(item)

for x in mylist:
	print(x)

if "apple" in mylist:
	print("yes")
	
else:
	print('no')

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)

item= mylist.remove("cherry")

print(mylist)
