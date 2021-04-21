#Fstring and string formatting
import math

me="abhijeet"
a=2
# c="This is {1} {0}"
# b=c.format(me,a)
# print(b)
c=f"This is {me} {a} {math.cos(37)}"
print(c)