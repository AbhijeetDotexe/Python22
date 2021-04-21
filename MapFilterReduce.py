#Map filter
n=["3","34","64"]
n=list(map(int,n))
# for i in range(len(n)):
#     n[i]=int(n[i])
n[2]=n[2]+32
print(n[2])
# def sq(a):
#     return a*a
#
# num=[2,3,4,5,6,7,8,9]
# square=list(map(sq,num))
# print(square)

# num=[12,13,14,15,16,17,18,19]
# square=list(map(lambda x:x*x,num))
# print(square)

# def sq(a):
#     return a*a
# def cu(a):
#     return a*a*a
# fun=[sq,cu]
# num=[12,13,14,15,16,17,18,19]
# for i in num:
#     val=list(map(lambda x:x(i),fun))
#     print(val)


#******************************************** FILTER ***************************************************************
num=[1,2,3,4,12,13,14,15,16,17,18,19]
def greater(n):
    return n>5
gr_than_5=list(filter(greater,num))
print("Number greater than 5 are :",gr_than_5)

#****************************************** REDUCE ****************************************************************
from functools import reduce
li=[1,2,3,4]
num= reduce(lambda x,y:x+y,li)
print("The SUm Of All The Numbers is : ",num)
