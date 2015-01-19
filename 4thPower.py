def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    x = x**2
    return x

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    x = square(square(x))
    return x

x=fourthPower(4)

print x
print 'number 2' 4**4    