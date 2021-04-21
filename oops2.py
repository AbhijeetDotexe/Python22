#   Classes and Objects(OOPS)

# Classes - Template
# Object- Instance of class which is capable of storing data of class type
# DRY- DO NOT REPEAT YOURSELF

class Employee:
    no_of_leaves=8
    pass
lakshay=Employee()
priyanshu=Employee()

lakshay.name="LAKSHAY"
lakshay.salary=10000
lakshay.role="INSTRUCTOR"

priyanshu.name="PRIYANSHU"
priyanshu.salary=20000
priyanshu.role="INSTRUCTOR"

print(lakshay.no_of_leaves)
Employee.no_of_leaves=9
print(Employee.no_of_leaves)

print(lakshay.__dict__)
lakshay.no_of_leaves=20
print(lakshay.__dict__)
print(Employee.__dict__)