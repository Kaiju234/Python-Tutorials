mytuple = ("Max",28,"Boston")
print(type(mytuple))

item = mytuple[-1]
print(item)

for x in mytuple:
	print(x)

if "Max" in mytuple:
	print("yes")
else:
	print("no")

my_tuple2 = ('a', 'p', 'p' 'l' 'e')

print(len(my_tuple2))

print(my_tuple2.count('a'))
print(my_tuple2.count('p'))
print(my_tuple2.count('p'))
print(my_tuple2.count('l'))
print(my_tuple2.count('e'))

print(my_tuple2.index('a'))

my_list = list(mytuple)
print(my_list)

my_list = list(my_tuple2)
print(my_list)

a=(1,2,3,4,5,6,7,8,9,10)

b=a[2:5]
print(b)

