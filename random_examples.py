import random
import secrets
import numpy as np
# random module functions

a = random.random()
print(a)
b = random.uniform(1,100)
print(b)
c = random.randint(1,10)
print(c)
d = random.randrange(1,10)
print(d)
e = random.normalvariate(0,1)
print(e)



# list examples with random module
myList = list("1234567")
print(myList)

f = random.choice(myList)
print(f)

g = random.sample(myList,6)
print(g)

h = random.shuffle(myList)
print(myList)


# random seed methods 

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))


# secrets module examples

a = secrets.randbelow(10)
print(a)

b = secrets.randbits(4)
print(b)

ProList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
c = secrets.choice(ProList)
print(c)

# random module with numpy
a = np.random.rand(3,5)
print(a)

b = np.random.randint(0,10,3)
print(b)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))

np.random.seed(1)
print(np.random.rand(3,3))