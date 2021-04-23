import math
# help(math)
v=4.35
print(v.__floor__())
print(v.__ceil__())
print(math.ceil(7.23))
print(math.floor(6.23))
print(math.e)
print(math.log(math.e))

print(math.sin(47))
print(math.cos(45))

import random
print(random.randint(9,10))
#
# random.seed(101)
# d=random.randint(0,100)
# print(d)
#
# l=list(range(0,20))
# print(l)
# print(random.choice(l))
#
# #with duplication
# print(random.choices(population=l,k=10))
#
# # WITHOUT DUPLICATION
#
# print(random.sample(population=l,k=10))
#
# e=random.shuffle(l)
# print(e)
# print(random.shuffle(l))

print(random.uniform(10,44))

print(random.gauss(mu=2,sigma=1))