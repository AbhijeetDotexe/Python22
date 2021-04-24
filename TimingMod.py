

def fun(n):
    return[str(num) for num in range(n)]

#print(fun(10))

def fun2(n):
    return list(map(str,range(n)))

#print(fun2(20))
# import time
#
# start = time.time()
#
#
# print(start)
# result=fun(10000000)
# end=time.time()
# print(end)
# final=end-start
# print(final)

import timeit

stmt="""
    fun3(100)

"""

setup='''
def fun3(n):
    return[str(num) for num in range(n)]

'''
print(timeit.timeit(stmt,setup,number=1000000))


stmt2='''
fun4(100)
'''
setup2='''
def fun4(n):
    return list(map(str,range(n)))

'''
print(timeit.timeit(stmt2,setup2,number=1000000))
