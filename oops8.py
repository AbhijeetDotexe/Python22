
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




    @staticmethod
    def printgood(string):
        return f"This is good {string}"

class Player:
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"Name is {self.name}, Game is {self.game} "

class Coolprogrammer(Employee,Player):
    pass



class Programmer(Employee):
    def __init__(self, aname , asalary , arole , languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages=languages




    def printporg(self):
        return f"Programmer's Name is {self.name}, Salary is {self.salary} and role is {self.role}, The languagen known is {self.languages}"


lakshay=Player("LAKSHAY",["FOOTBALL"])
Abhijeet=Coolprogrammer("ABHIJEET",90009,"COOL PROGRAMMER")
det=Abhijeet.printdetails()
print(det)


