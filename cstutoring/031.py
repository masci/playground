"""
Given the first few factorials below:

1! = 1
2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6
4! = 4 x 3 x 2 x 1 = 24

etc...

How many zeros appear in total in 100!?
"""
def fact(n):
    ret = 1
    while n:
        ret *= n
        n -= 1
    return ret

print str(fact(100)).count('0')