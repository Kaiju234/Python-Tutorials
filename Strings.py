my_string = "Hello World"
print(my_string)
my_string = """Hello
World"""
print(my_string)

my_string = "Hello World"
substring = my_string[::-1]
print(substring)

name = "Tom"

greeting = "Hello"
sentence = greeting + " " + name
print(sentence)

for x in greeting:
	print(x)

greeting = "hello"
if "g" in greeting:
	print("yes")
else:
	print('no')

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)

new_string = ''.join(my_list)
print(new_string)

my_list = ["a"] * 6
print(my_list)

my_string = ''
for i in my_list:
	my_string += i
print(my_string)

from timeit import default_timer as timer
my_list = ['a'] * 6
print(my_list)

start = timer()
my_string = ''
for i in my_list:
	my_string += i
stop = timer()
print(stop - start)

my_string = ''.join(my_list)
print(my_string)

