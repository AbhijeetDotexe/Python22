# Tuples
# Tuple is an ordered data type which is immutable and allows duplicate elements
mytuple=("Lakshay",4,"Uttrakhand")
print(mytuple)
# To print single element in a tuple mytuple=('Lakshay",) u need to insert a comma even if u use a single element

mytuple1=tuple(["Priyanshu",4,"Uttrakhand"])
print(mytuple1)

for i in mytuple1:
    print(i)

if "Priyanshu" in mytuple1:
    print("yes")
else:
    print("Oh no !")

# print(len(mytuple1))

my_tuple=('a','b','c','d','e','f','g','h','i','j')
print(my_tuple.index('a'))
print(my_tuple.index('d'))
print(my_tuple.index('e'))
print(my_tuple.index('b'))
print(my_tuple.index('j'))

my_l=list(my_tuple)
print((my_l))


a=(1,2,3,4,5,6,7,8,9)
b=a[2:5]
print(b)
c=a[::2]
d=a[::-1]
print(c)
print(d)



my_tu = "Lakshay",4,"Kotdwar"
name,age,city=my_tu
print(name)
print(age)
print(city)

my_tp=(0,1,2,3,4,5,6,7,8,9)

i1,*i2,i3=my_tp
print(i1)
print(*i2)
print(i3)

import sys
my_lis=[0,1,2,"hello",True]
my_tup=(0,1,2,"hello",True)
print(sys.getsizeof(my_lis),"bytes is the size of the list")
print(sys.getsizeof(my_tup),"bytes is the size of the tuple")


import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]",number=10000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)",number=10000000))