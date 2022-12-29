myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())


print(myset)

for x in myset:
	print(x)

if 1 in myset:
	print("yes")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.symmetric_difference(setB)
print(diff)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

setC = {1,2,3,4,5,6,}
setD = {1,2,3}
setE = {7,8}

print(setC.issubset(setD))

print(setD.issuperset(setC))

print(setC.isdisjoint(setD))

setF = {1,2,3,4,5,6,}

setG = setF 

setG.add(8)
print(setG)
