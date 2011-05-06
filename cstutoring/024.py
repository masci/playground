"""
Given the definition of a mathematical combination:

n C r

where n is the total number of selections and r is the number you are choosing 
from the pool.

The formula for evaluation is:

      n!
   ---------
   r! (n-r)!

What is the answer when you evaluate the following expression:

17 C 10 - 30 C 12 + 50 C 3
"""
def factorial(n):
    p = 1
    while n>1:
        p *= n
        n -= 1
    return p

def combi(a,b):
    return factorial(a) / (factorial(b) * factorial(a-b))

print combi(17,10) - combi(30,12) + combi(50,3)