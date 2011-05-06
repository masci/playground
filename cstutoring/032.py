"""
Given the first few Fibonacci numbers below:

1 1 2 3 5 8 13 21 ...

How many of the first 250 Fibonacci numbers are prime? 
Note that you are seeing the first 8 above.
"""
import math
import random

def isprime(n):
    n = abs(int(n))
    # 0, 1
    if n < 2: return False
    # 2 is the only even prime
    if n == 2: return True
    # evens are not prime
    if not n & 1: return False
    # for odds
    # range starts with 3 and only needs to go up the squareroot of n
    for x in xrange(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

def isPrime(n):  
    n = abs(int(n))
    if n < 2: return False
    if not n & 1: return False
    s, r = n-1, 1  

    # Step 1: Calculate s and r  
    while not s&1:  
        s >>= 1  
        r  += 1  

        # Test the number 10 times  
        for i in range(0,10):  
            # Step 2 & 3: Calculate a^s mod n,  
            # where a is a random number  
            y = pow(random.randint(1,n-1),s,n)  

            # Step 3: If y equals 1, n passed the  
            # test this time  
            if y == 1:  
                continue  

            # Step 4: If the first test failed,  
            # try values of j from 1 to r-1  
            for j in range(1,r):  
                # Step 4: If y = n-1, n passed the test  
                if y == n-1:  
                    break  

                # Step 4: Rather than calculate a^((2^j)*s)  
                # mod n, we can take this shortcut  
                y = pow(y,2,n)  
            else:  
                # If y never equaled n-1, then n is composite  
                return False  

        # n passed all of the tests, it is very  
        # likely prime  
        return True

def fiborange(limit):
    n, f = 0, 1
    while (f <= limit):
        yield f
        n, f = f, f+n

def main():
    count = 0
    f = fiborange(10**100)
    for x in xrange(251):
        if isPrime( f.next() ): 
            count += 1
    print count

if __name__ == "__main__":
    main()

