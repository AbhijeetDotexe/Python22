# Strings ordered, immutable,text represnetation
# my_str = "Hello World !"
# print(my_str)
# # Use escape character like this \ if u want to use single quotes
#
# my_string = """ How are
# you"""
# print(my_string)
# char = my_str[0]
# print(char)
#
# substring = my_str[1:5]
# print(substring)
#
# sub=my_str[::-1]
# print(sub)
#
# greeting = "Hello"
# name = "Lakshay"
# sentence = greeting + " " + name
# print(sentence)
#
# for i in greeting:
#     print(i)
# if 'e' in greeting:
#     print("yes")
# else:
#     print("NO")
#
#
# str1 = "            Hello world              "
# print(str1)
# str1= str1.strip()
# print(str1)
#
# print(str1.upper())
# print(str1.startswith("H"))
# print(str1.endswith("H"))
# print(str1.find('o')) # If it doesnt not find any string it returns -1
# print(str1.count('l'))
# print(str1.replace('Hello', 'Universe'))






my_str = 'How are you doing'
my_list = my_str.split(" ")
print(my_list)

new_str = " ".join(my_list)
print(new_str)

from timeit import default_timer as timer


l=['a'] *1000000
#print (l)
start = timer()
str1 = " "
for i in l:
    str1 += i
stop =timer()
print(stop-start) # This is bad because it is very expensive as string is immutable it creates a new string everytime

start= timer()
my_str1 = "".join(l)
stop = timer()
print(stop - start) # this is good

# string formatting
var= "Lakshay"
str2 = " The Variable is %s " % var  # use %d for numbers(decimal value) and %f for floating point value
print(str2)


str3="The variable name is {} ".format(var)
print(str3)