""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Performance note: try to comment out the part of check_prime which test only
numbers < sqrt(i) and see what happens to the performances
"""

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
        
if __name__ == "__main__":
    # an empty list to contain primes as we found 'em
    primes = []
    i = 2
    # stop at this point
    top = 10001
    while len(primes) < top:
        if check_prime(i, primes):
            primes.append(i)
        i += 1
    
    print primes[-1]