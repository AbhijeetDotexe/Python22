# DECORATORS
# def fun1():
#     print("HELLO EVERYONE !")
# fun2=fun1
# del fun1
# fun2()


# def fun3(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=fun3(1)
# print(a)

def dec1(func1):
    def nowexec():
        print("EXECUTING NOW")
        func1()
        print("EXECUTED")
    return nowexec
@dec1
def who_is_lakshay():
    print("Lakshay is a very good boy")

#who_is_lakshay=dec1(who_is_lakshay)
who_is_lakshay()













