"""
In math, a prime number is a number only divisible by 1 and itself.

Given the first few prime numbers

2 3 5 7 11 13 17 ...

What is the sum of the first 250 prime numbers?
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

def build_primes(limit):
    primes = []
    i=2
    while len(primes) < limit:
        if check_prime(i,primes): primes.append(i)
        i+=1
    return primes

def main():
    print sum(build_primes(250))

if __name__ == "__main__":
    main()