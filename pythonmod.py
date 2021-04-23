from collections import Counter
my_list=[1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
print(Counter(my_list))
m=my_list


from collections import namedtuple
Dog=namedtuple("DOG",["age","breed","name"])
Sammy=Dog(age=5,breed="Husky",name="sammy")
print(Sammy)
print(type(Sammy))
print(Sammy.name)
print(Sammy.age)