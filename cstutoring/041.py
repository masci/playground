"""
Given the first few prime numbers below:

2 3 5 7 11 13 17 ...

How many primes under 1,000,000 have the sum of the factorials of their digits 
equal to another prime number?
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

def fact(n):
    ret = 1
    while n:
        ret *= n
        n -= 1
    return ret

factorials = {}
def get_fact(n):
    return factorials.setdefault(n, fact(n))

def main():
    ok = [2]
    for i in xrange(3, 10**6, 2):
        if not isprime(i): 
            continue
        s=0
        for d in str(i):
            s+=get_fact(int(d))
        if isprime(s): 
            ok.append(s)
    print len(ok)

if __name__ == "__main__":
    t = time.time()
    main()
    print time.time() - t
