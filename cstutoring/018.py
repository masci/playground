"""
In math, a prime number is only divisible by 1 and itself

Given the first few primes below:

2 3 5 7 11 13 17 ...

How many of the primes below 1,000,000 have the sum of their digits equal to 
the number of days in a fortnight?
"""
import time

def check_prime(i, primes):
    """ Check if given number is prime by trying to divide it for every prime
        found up until now and contained in 'primes' parameter
    """
    is_prime = True
    for p in primes:
        if i%p == 0:
            is_prime = False
        # we can stop searching if p is greater than the sq root of i
        if p*p > i or not is_prime:
            break
        
    return is_prime

def build_primes(limit):
    primes = [2]
    i=3
    while i < limit:
        if check_prime(i,primes): primes.append(i)
        i+=2
    return primes

def main():
    tot = 0
    for p in build_primes(10**6):
        if sum(int(x) for x in str(p)) == 14: tot+=1
    print tot

if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print (t2-t1)*1000

