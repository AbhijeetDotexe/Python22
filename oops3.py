#   Classes and Objects(OOPS)

# Classes - Template
# Object- Instance of class which is capable of storing data of class type
# DRY- DO NOT REPEAT YOURSELF

class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary=asalary
        self.role=arole


    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"
lakshay=Employee("LAKSHAY",20000,"INSTRUCTOR")
# lakshay=Employee()
# priyanshu=Employee()
#
# lakshay.name="LAKSHAY"
# lakshay.salary=10000
# lakshay.role="STUDENT"
#
# priyanshu.name="PRIYANSHU"
# priyanshu.salary=20000
# priyanshu.role="INSTRUCTOR"
#
# print(lakshay.printdetails())
# print(priyanshu.printdetails())
#
# print(lakshay.no_of_leaves)
print(lakshay.name)
print(lakshay.role)
print(lakshay.salary)
