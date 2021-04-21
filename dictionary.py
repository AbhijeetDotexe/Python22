#Dictionary is nothing but key value pairs
#d1={}
#print(type(d1))
d2={"Lakshay":"Burger","Abhijeet":"Roti","Priyanshu":{"B":"Bread", "L":"Pizza","D":"Chicken"}}
#print(d2["Priyanshu"]["B"])
d2["Gabru"]="Junk food"
print(d2)
del d2["Gabru"]
print(d2)
d3=d2.copy()
del d3["Abhijeet"]
print(d3)
print(d2.keys())
print(d2.items())