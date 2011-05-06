"""
In math, a positive number n is a perfect square if:

(floor( sqrt(n) ) )^2 = n

A perfect square is defined below using the above rule:

where n = 4

(floor( sqrt(4) ))^ 2 = 4
(floor( 2 ))^ 2 = 4
(2)^2 = 4
4 = 4  --> PERFECT

A non perfect square is defined below using the above rule:

where n = 7

(floor( sqrt(7) ))^ 2 = 7
(floor( 2.64575131 ))^ 2 = 7
(2)^2 = 7
4 = 7  --> NOT PERFECT

What is the sum of the square roots of all non-perfect squares for all 
n (2 <= n <= 10,000)?

Enter the answer rounded to the nearest whole number.
"""
import math

def check_perfect(n):
    return math.floor(math.sqrt(n))**2 == n

res = 0
for i in xrange(2, 10000):
    if not check_perfect(i):
        res += math.sqrt(i)

print res