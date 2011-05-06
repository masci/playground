"""
Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""

N = 100
print sum(xrange(1,N+1))**2 - sum(x**2 for x in xrange(1,N+1))