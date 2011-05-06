"""
Given the first few Fibonacci numbers:

1 1 2 3 5 8 13 ...

What is the sum of the first 75 Fibonacci numbers?

As an example above, the sum of the first 7 numbers is 33.
"""
def fiborange(limit):
    n, f = 0, 1
    while (f <= limit):
        yield f
        n, f = f, f+n

i=0
fibo_sum=0

for x in fiborange(10**20):
    fibo_sum += x
    i+=1
    if i == 75: break

print fibo_sum,i