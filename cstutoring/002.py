""""
As an example, the sum of the digits of 2 to the 10th power is:

2^10 = 1024  => 1+0+2+4 => 7

What is the sum of the digits of 2^50?
"""

print sum(int(x) for x in str(2**50))
