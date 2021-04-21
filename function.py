#Functions and Docstrings
a=9
b=6
c= sum((a,b))#Built in Function
print(c)

def function1():
    print("Hello you are in function 1")

print(function1())

def function2(a,b):
    """This is a function which calculates average of two numbers
    and this function doesn't work for three numbers"""
    average=(a+b)/2
    #print(average)
    return average

v=function2(5.64,7.57)
print(v)

