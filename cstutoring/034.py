"""
Jack has a stack of index cards with the first 25 prime numbers. 
John has a stack of index cards with the first 25 Fibonacci numbers.

What is the probability that, when they both choose a number, that Jacks 
number is a sub string of Johns number. As an example below:

Jack chooses -->   5
John chooses -->   233
NO

Jack chooses -->   59
John chooses -->   1597
YES

Enter the number in the form 0.XXXX where X is the digits of the answer.
"""
def fiborange(limit):
    n, f = 0, 1
    while (f <= limit):
        yield f
        n, f = f, f+n

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

john = []
f = fiborange(10**20)
for x in xrange(25):
    john.append(f.next())

jack = build_primes(25)

occurr = {}

for p in jack:
    for f in john:
        if str(f).count(str(p)):
            occurr[p] = occurr.setdefault(p, 0) + 1

p = 0.0

for v in occurr.values():
    p += v/25.0

print p/25.0
