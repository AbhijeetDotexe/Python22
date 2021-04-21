#Q. Take input from a user till he doesn't enter a number which is grater than 100
while(True):
    inp=int(input("Enter a number"))
    if inp>100 :
        print("Congrats you have Entered a number which is greater than 100\n")
        break
    else:
        print("Try again\n")
        continue

