#Fibonacci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

num=int(input("Enter the number of elemts in the series : "))
print(fib(num))