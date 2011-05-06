"""
Given the first few Fibonacci numbers:

1 1 2 3 5 8 13 21 ...

How many odd digits (1, 3, 5, 7 or 9) are contained in the 1000th Fibonacci 
number?
"""
def fiborange(limit):
    n, f = 0, 1
    while (f <= limit):
        yield f
        n, f = f, f+n

f = fiborange(10**500)
num = 0
for x in xrange(1000):
    num = f.next()

dgt = 0
for d in str(num):
    if int(d) % 2: 
        dgt+=1

print dgt