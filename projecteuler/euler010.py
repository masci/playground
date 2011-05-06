from euler007 import check_prime

""" Find the sum of all the primes below two million.
"""

primes = []

for i in range(2,2000000):
    
    if check_prime(i, primes):
        primes.append(i)
    
    i += 1

print sum(primes)
    
