# Lambda functions or Anonymous functions
#lambda is one liner function
# minus = lambda x,y: x-y
# print(minus(9,5))

def a_first(a):
    return a[1]

a=[[1,24],[2,15],[3,6],[4,7]]
a.sort(key=a_first)
print(a)
#a.sort=(key=lamda x:x[1])