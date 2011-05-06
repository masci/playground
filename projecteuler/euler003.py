""" What is the largest prime factor of the number 600851475143 ?
"""
import time

def factorize(n):
    """ prime factorization implemented with trivial trial division method
        complexity should be sqrt(n)/2 or something similar
    """
    factors = {}
    checker = 2
    newn = n
    while checker*checker <= newn:
        if newn % checker == 0:
            factors[checker] = factors.setdefault(checker,0) + 1
            newn = newn / checker
        else:
            checker = checker+1
            
    if newn != 1:
        factors[newn] = 1
        
    return factors
    
if __name__ == '__main__':
    t1 = time.time()
    res = max(factorize(600851475143).keys())
    t2 = time.time()
    print res,(t2-t1)*1000
