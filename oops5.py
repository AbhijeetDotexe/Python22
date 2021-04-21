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

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_str(cls,string):
        params=string.split("-")
        #return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
lakshay=Employee("LAKSHAY",20000,"INSTRUCTOR")
priyanshu=Employee("PRIYANSHU",40000,"INSTRUCTOR")
shaani=Employee.from_str("SHAANI-500-STUDENT")
Employee.no_of_leaves=40

lakshay.change_leaves(60)# CLASS METHODS
print(shaani.salary)
# print(priyanshu.no_of_leaves)
# print(lakshay.no_of_leaves)