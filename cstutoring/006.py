"""
Given the following function and it's results:

f(x,y) = x^y + y^x where x>0 and y>1

f(1,2) = 1^2 + 2^1 = 3
f(2,3) = 2^3 + 3^2 = 17
f(3,4) = 3^4 + 4^3 = 145
.
.
.
Using the above function denoted by f(x,y), and given that the initial values
of x = 1 and y = 2, which increase by 1 each time, what are the last 4 digits
of the sum of the first 15 function calls.
"""
def fxy(x,y):
    return (x**y)+(y**x)

print str(sum(fxy(x,x+1) for x in xrange(1,16)))[-4:]