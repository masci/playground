"""
What is the sum of the digits of 1000!? (One Thousand Factorial). 
"""
import time

def fact(n):
    r = 1
    while n>1:
        r *= n
        n -=1
    return r

t = time.time()
print sum(int(x) for x in str(fact(1000)))
print "elapsed time: %f " % (time.time() - t)