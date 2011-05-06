"""
What is the sum of the factorials of each digit in 100!? (Hint: solve problem 
31 first so you can compute 100!).

An example is below showing 5! Your task is to use 100!

5! = 120
1! + 2! + 0! = 4

The answer is 4.
"""
def fact(n):
    if n == 0: return 1
    ret = 1
    while n:
        ret *= n
        n -= 1
    return ret

print sum( fact(int(x)) for x in str(fact(100)) )