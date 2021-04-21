#Q. Check the age of the user for driving license ?
print("Enter Your Age:")
age=int(input())
l=18
if age>l:
    print("You are eligible for driving")
elif age<l:
    print("You are not eligible for driving ")
else:
    print("You have to come to the Office then we will decide if you are eligible or not ")
