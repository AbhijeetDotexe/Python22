#Global variables
#l=10 #Global variable
#def function1(n):
    #l=5
   # m=8
#     global l
#     l=l+45
#     print(l)
#     print(n,"I have printed the number")
# function1("This is me")



def Abhijeet():
    x = 20
    def lakshay():
        global x
        x=88
    print("before calling lakshay()",x)
    lakshay()
    print("after calling laskhay()",x)
Abhijeet()