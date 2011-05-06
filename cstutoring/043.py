"""
A hexagonal number is computed as follows using the formula:

H(n) = n(2n-1)

As shown, the first 5 hexagonal numbers are:

1 6 15 28 45

How many of the first 100,000,000 hexagonal numbers are divisible by all the 
numbers from 1 through 20?
"""
import time

def hexagonal(n):
    return n*(2*n-1)
    
def good(n):
    for x in xrange(20,10,-1):
        if n%x != 0: return False
    print n
    return True

t1 = time.time()
he = set( x for x in xrange(2, 100000001, 2) if good(hexagonal(x)) )
print len(he)
print time.time() - t1