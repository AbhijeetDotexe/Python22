# Itertools: products, permutation, combination, accumalate, groupby and infinite iterators
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)
print(list(prod))

from itertools import permutations
c = [1,2,3]
perm = permutations(c)
print(list(perm))

from itertools import combinations
comb=combinations(c,2)
print(list(comb))

from itertools import  accumulate
acc = accumulate(c)
print(list(acc)) # the next digit is the sum of the previous digits

from itertools import  groupby
d = [1,2,3,4,5]
def samller_than_3(x):
    return  x < 3
grp = groupby(d,key =samller_than_3 )
print(grp)

for key,value in grp:
    print(key, list(value))

from itertools import  count , cycle, repeat

for i in count(10):
    print(i)
    if i ==  15:
        break