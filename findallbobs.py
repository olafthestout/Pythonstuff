
s='bobinbobbobber3bobert4bobert5'

def fb(s):
    c = 0
    n = 'bob'
    for x in xrange(len(s) - len(n) + 1):
           if s[x:x+len(n)] == n:
                c += 1
    return c
         
print('Number of times bob occurs is: ' + str(fb(s)))