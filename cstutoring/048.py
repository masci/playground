"""
Let p be a prime number. For p>3 there is a formula f=6*k + or - 1, which 
means each prime is of the form f.

With k=1: f-1=5 and f+1=7 are primes. But there are many k's which do not make 
a prime, e.g. with k=20: f-1=119 and f+1=121 are not primes!

For all primes 5 < p < 3000 what is the sum of all k's which do not build a 
prime.
"""

def isprime(n):
    n = abs(int(n))
    if n < 2:  return False
    if n == 2: return True
    if not n & 1: return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    
    return True

def f(n):
    p1 = 6*n-1
    p2 = 6*n+1
    return (isprime(p1) or isprime(p2), p2)

tot=0
k=1
while f(k)[1] < 3000:
    if not f(k)[0]:
        tot+=k
    k+=1

print tot
        