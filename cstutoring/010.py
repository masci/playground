"""
What is the sum of all prime numbers below 5000? 
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
    print sum(build_primes(5000))

if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print (t2-t1)*1000
