add20 = lambda x: x + 10
print(add20(5))

sub50 = lambda x: x - 50
print(sub50(4))

mult = lambda x,y: x * y 
print(mult(2,7))

points2D = [(1,2),(3,6),(7,8),(8,10)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)
points2D
def sort_by_y(x):
	return x[1]
points2D_sorted = sorted(points2D,key = lambda x: x[1])



a = [1,2,3,4,5]
b = map(lambda x: x+2, a) 
print(list(b))

a = [1,2,3,4,5]
b = filter(lambda x: x%2, a) 
print(list(b))

c = [x for x in a if x%2==0]
print(c)

from functools import reduce
a = [1,2,3,4,5,6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)


