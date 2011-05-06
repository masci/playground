"""
The standard Fibonacci sequence is represented by the sum of the previous 2 
terms. Generally, it can be expressed as:

Fn = Fn-1 + Fn-2

Just as well, we can express an X-nacci sequence where the next number is the 
sum of the previous X number of terms. The general form for this would be:

Fn = Fn-1 + Fn-2 + ... + Fn-x

The sequence for any X-nacci always begins with the first X terms being 1. So 
for a 4-Nacci sequence the start would be:

1 1 1 1 4 7 13 25 ...

But realizing that the values of any X-nacci sequence terms get large rather 
quickly, we want to mod the resulting number by 1,000,000 to keep the values 
of the terms from 0 to 999,999. The formula will still be the same except you 
need to mod the result:

Fn = (Fn-1 + Fn-2 + ... + Fn-x) MOD 1,000,000

How many of the first 1,000,000 terms of a 25-nacci sequence that is modded 
by 1,000,000 are prime?
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

def x_nacci_gen(limit):
    last = [1]*25
    i=1
    while i < limit:
        if i <= 25: r=1
        else:
            r = sum(last)%10**6
            last.append(r)
            last = last[1:]
        yield r
        i+=1

count = 0
for x in x_nacci_gen(10**6):
    if isprime(x): count+=1

t = time.time()
print count,time.time()-t

