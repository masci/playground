from euler07 import check_prime

""" A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

primes = []

def build_primes(limit):
    
    for i in range(2,limit):
        if check_prime(i, primes):
            primes.append(i)
        i += 1
    
    return primes    

def sum_pyth_triple(m, n):
    a = (m*m) - (n*n)
    b = 2*m*n
    c = (m*m) + (n*n)
    
    return a+b+c

def print_pyth_triple(m, n):
    a = (m*m) - (n*n)
    b = 2*m*n
    c = (m*m) + (n*n)
    
    print a,b,c
    print a*b*c

def gcd(m,n):
    if n==0: return m
    else: return gcd(n, m%n)

def is_coprime(m,n):
    return gcd(m, n) == 1
    
if __name__ == "__main__":
    for n in range(1, 30):
        for m in range(n+1, 30):
            if sum_pyth_triple(m,n) == 1000:
                print_pyth_triple(m,n)
    