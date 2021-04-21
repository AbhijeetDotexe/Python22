#Create a dictionary and take input from the user and return the meaning of the word from dictionary
print("Welcome to dictionary")
d1={"Penance":"Tapasya","Austerity":"Kathor","Turmoil":"Ashanti","Godhead":"Bhagwan","Lamentation":"Vilap"}
print(d1.keys())
print("Enter the word you want to find the meaning of:")
meaning=(input())
print("The meaning of the word is")
print(d1[meaning])
print("Thank you for using our dictionary")
