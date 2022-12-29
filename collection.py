from collections import Counter
a = "Dragoon"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))


from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4,5,6])

d.extendleft([4,5,6])

d.rotate(2)
print(d)
