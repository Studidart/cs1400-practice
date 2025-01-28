#problem2-1-1
def sum():
    x=10
    y=20
    print(x+y)
#sum()

#problem2-1-2
def product():
    a=10
    b=20
    print(a*b)
#product()

#problem2-1-3
def product(a,d=2):
    print(a*d)
#product(4)
#product(4,6)

#challenge2-1-1
#there is no minumum amount of parameters.

#challenge2-1-2
def broken(a,b):
    return a+b

broken()
#returned: Exception has occurred: TypeError
#broken() missing 2 required positional arguments: 'a' and 'b'
#  File "/Users/26combsrobc/Documents/problems 2/problem2-1.py", line 28, in <module>
#    broken()
#TypeError: broken() missing 2 required positional arguments: 'a' and 'b'