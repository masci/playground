"""
Mr. Red has 50 red discs; Mr. Blue has 75 blue discs and Mr. Green has 100 
green discs.

Mr. Red's discs contain the first 50 prime numbers. Mr. Blue's discs contain 
the first 75 Fibonacci numbers and Mr. Green's discs contain the first 100 
triangle numbers.

What then is the probability that when each person randomly draws a disc, each 
disc will be an odd number and Mr. Red's discs will end with a 7?

Enter the number in the form 0.XXXX rounded to the nearest 10,000th where X is 
the digits of the answer.
"""
import time

def isprime(n):
    n = abs(int(n))
    if n < 2:  return False
    if n == 2: return True
    if not n & 1: return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    
    return True

def fiborange(limit):
    n, f = 0, 1
    while (f <= limit):
        yield f
        n, f = f, f+n

def triangle(n):
    return n*(n+1)/2

####

reds=[2]
i=3
while len(reds) < 50:
    if isprime(i): reds.append(i)
    i+=2

blues = []
for i,x in enumerate(fiborange(10**100)):
    if (i==75): break
    blues.append(x)

greens = [triangle(x) for x in xrange(1,101)]

####

p_reds = len([x for x in reds if x%10==7])/50.0
p_blues = len([x for x in blues if x%2!=0])/75.0
p_greens = len([x for x in greens if x%2!=0])/100.0

print p_reds*p_blues*p_greens
