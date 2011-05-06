"""
The reciprocal value for N = 2 is
1/N = 1/2 = 0.5 .
Which is a terminating decimal number with periodlength L=0.

The reciprocal value for N =3 is
1/N = 1/3 = 0.3333333333333 .
Which is a non-terminating decimal number with periodlength L=1.

The reciprocal value for N = 7 is
1/N = 1/7 = 0.142857142857 .
Which is a non-terminating decimal number with periodlength L= N-1 = 6.

Find all primes of N in the interval 1<=N<=3000 where reciprocal value 1/N has 
a periodic decimalquotient with period length L=N-1. How many of these numbers 
occur? (simply give the count).
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

def find_prime_period(n):
    if n < 7: return 0
    if not isprime(n): return 0

    trial = '9'
    while int(trial) % n != 0:
        trial += '9'
    return len(trial)

t1 = time.time()
count=0
for i in xrange(7,3001,2):
    if find_prime_period(i) == i-1:
        count += 1
t2 = time.time()

print count, t2-t1
