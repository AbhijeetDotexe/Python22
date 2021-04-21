#args and kwargs( arguments and key word arguments
# def name_print(a,b,c,d):
#     print(a,b,c,d)
# name_print("Abhijeet","Lakshay","Priyanshu","Shaani")
def funargs(n,*args,**kwargs):#It is always of type tuple
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(key,value)
a=["Abhijeet","Lakshay","Priyanshu","Shaani","Nonu"]
n="Different names of lakshay are : "
k={"Lakshay":"Name 1","Priyanshu":"Name 2","Shaani":"Name 3","Nonu":"Name 4"}
funargs(n,*a,**k)#Normal arguments should be placed first everytime else it will give an error


