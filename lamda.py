# lambda arguments : expression

x = lambda a:a + 10 
print(x(10))
y = lambda s:s * 20
print(y(2))

# can take any number of arguments
x = lambda a, b, c : a +b +c * 8
print(x(12,2,3))

def myfunc(n):
    return lambda a:a * n
mydoubler = myfunc(2)
print (mydoubler(11))

mytriple = myfunc(3)
print (mytriple(11))