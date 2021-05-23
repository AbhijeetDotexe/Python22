# Lambda functions
add10 =  lambda x: x + 10
print(add10(13))

mult = lambda x,y: x*y
print(mult(2,11))

point2d = [(1,2),(15,1),(3,-5),(7,21),(0,5)]
sor = sorted(point2d, key = lambda  x:x[-1]) # sort by second index value
sr = sorted(point2d)
print(point2d)
print(sor)
print(sr)

a = [1,2,3,4,5,6]
b = map(lambda x:x*2, a)
print(list(b))

c = [x*2 for x in a ]
print(c)

b = filter(lambda x:x%2 == 0, a)
print(list(b))

d = [x for x in a if x%2 == 0]
print(d)

e = [1,2,3,4,5,6]
from functools import  reduce
prod_e = reduce(lambda x,y: x*y, a)
print(prod_e)