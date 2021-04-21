#Faulty calculator
#45*3= 555, 56+9=77, 56/6=4
print("Welcome to The Calculator")
print("Enter Number 1:")
a=int(input())
print("Enter Number 2:")
b=int(input())
print("Enter the operator (+,-,*,/)")
c=(input())
if a==45 and b==3 and c=="*":
    print("555")
elif a==3 and b==45 and c=="*" :
    print("555")
elif a==56 and b==9 and c=="+":
    print("77")
elif b==56 and a== 9 and c=="+":
    print("77")
elif a==56 and b==6 and c=="/":
    print("4")
elif b==56 and a==6 and c=="/":
    print("4")
elif c== "+" :
    print(a+b)
elif c=="-" :
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/" :
    print(a/b)

