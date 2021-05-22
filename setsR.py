# Sets are unordered,  mutable and there are no duplicate elements
myset = {1, 2, 3 }
print(myset)
mysets = [1, 2, 3 ]
print(mysets)
myset1 = set("Hello")
print(myset1)
# If you want to create an empty set
myset= set()
print(type(myset))

myset.add(4)
myset.add(5)
myset.add(6)
myset.add(7)
print(myset)

myset.remove(5)
print(myset)
# if the element is not in the list this will give an error
# so we use dot discard which removes the element if it is present and
# does not give any error if the element is not there
myset.discard(20)
print(myset)

#print(myset.pop())

for i in myset:
    print(i)

if 4 in myset:
    print("Yes it is present in the set " )
else:
    print("It is not present in the set ")


odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7, 11}

u = odds.union(even)
print(u)
i = odds.intersection(even)
print(i)

j=odds.intersection(primes)
print(j)

k = even.intersection(primes)
print(k)


setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3}

# diff = setA.difference(setB)
# print(diff)
#
# sydiff =setA.symmetric_difference(setB)
# print(sydiff)

#setA.update(setB)
#print(setA)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setB.issuperset(setA))
print(setA.isdisjoint(setB))

# copy works the same as in tuples if you modify the copy the original will also modify

a = frozenset([1,2,3,4])
print(a)
# Frozen sets cannot be modified they remain the same and will you give you and error if you try to modify them
