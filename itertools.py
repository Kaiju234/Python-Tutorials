from itertools import product
a = [1,2]
b = [3]
prod = product(a,b, repeat = 2)
print(list(prod))

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))

from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))

from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))

from itertools import groupby

def smaller_than_3(x):
	return x < 3

a = [1,2,3,4]
group_obj = groupby(a,key=lambda x: x<3)
for key, value in group_obj:
	print(key, list(value))
	

from  itertools import count,cycle,repeat 
a = [1, 2 ,3]
for i in cycle(a):
	print(i)

a = [1,2,3]
for i in repeat(1):
	print (i)
