#Q.create a list and display which are numbers and bigger than 6(List can be of anything)
l=["lakshay","Priyanshu","Abhijeet",int,float,7,9,11,25,89,2,3,5,99]
for item in l:
    if str(item).isnumeric() and item>6 :
        print(item)
        