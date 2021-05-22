# Dictionary key-value , unordered and immutable
mydict = {"Name": " Lakshay", "Age": 4,"city": "Uttrakhand"}
print(mydict)
mydict2=dict(Name="Priyanshu",Age=4,city="Uttrakhand")
print(mydict2)
value=mydict['Name']
print(value)
mydict["email"] = "Lakshay23@gmail.com"
print(mydict)
mydict["email"] = "coolboyLakshay23@gmail.com"
print(mydict)
mydict.pop("city")
print(mydict)

# if "Name" in mydict:
#     print(mydict["Name"])
#
#
# try:
#     print(mydict2["Name"])
# except:
#     print("Error !")
#
# for key in mydict:
#     print(key)
#
# for value in mydict.values():
#     print(value)

for key,value in mydict.items():
    print(key,value)

mydict_cpy = mydict
print(mydict_cpy)

# Moidifying the copy of the list also modifies the original dictionary
mydict_cpy["email"] = "Priyanshu23@gmail.com"
print(mydict)
print(mydict_cpy)

# if u just want to create a copy use the dot copy keyword
# mydict.copy

mydict.update(mydict2)
print(mydict)

my_dict = {3:9, 6:36, 9:81}
print(my_dict)

value=my_dict[3]
print(value)

mytuple = (8,7)
my_dict2 ={mytuple:15} # It only works with tuples it does not work with list 
print(my_dict2)