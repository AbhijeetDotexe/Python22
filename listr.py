 # List

# mylist=["banana","cherry","apple"]
# print(mylist)
# item = mylist[2]
# print(item)
# for i in mylist:
#     print(i)
# if "banana" in mylist:
#     print("yes")
# else:
#     print ("oh no!")
# mylist.append("lemon")
# print(mylist)
# mylist.insert(1,"blueberry")
# print(mylist)
#
# item = mylist.pop()
# print(item)
# print(mylist)
#
# item= mylist.reverse()
# print(mylist)
# item =mylist.sort()
# print(mylist)

# mylist=[0]*5
# print(mylist)
# mylist2=[1,2,3,4,5]
# newl=mylist+mylist2
# print(newl)


mylist=[1,2,3,4,5,6,7,8,9]
a=mylist[1:5]
print(a)

b=mylist[::-1]
print(b)

list_org=["banana","cherry","apple"]
list_copy=list_org
# if you modify the copy of the list the original list will also get modified if you dont use the dot copy keyword


list_copy.append("lemon")
print(list_copy)
print(list_org)

myl=[1,2,3,4,5,6,7,8,9]
b=[i*i for i in myl]
print(myl)
print(b)