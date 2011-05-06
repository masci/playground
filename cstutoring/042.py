"""
A triangle number is computed with the following formula:

T(n) = n(n+1)/2

Using the above formula, the first 5 triangle numbers are:

1 3 6 10 15 ...

What then is the sum of the digits of the 123,456,789th triangle number?
"""

def triangle(n):
    return str(n*(n+1)/2)

print sum( int(x) for x in triangle(123456789) )