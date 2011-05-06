"""     
Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.
"""

import time

class memoize:
    """ a class implementing memoization, to be used as a decorator
		see euler14.py to check out an alternative solution
    """
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]

@memoize
def fibonacci(n):
    """ trivial fibonacci implementation """
    if n in (0, 1): return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def solve():
    i=res=sum=0

    while res < 4000000:
        res = fibonacci(i)
        if (res%2) == 0: sum = sum + res
        i=i+1

    return sum

if __name__ == '__main__':
    t1 = time.time()
    s = solve()
    t2 = time.time()
    print s,(t2-t1)*1000
