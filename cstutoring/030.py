"""
Given the following sequence of numbers:

10000
sum (3n+2) / (2n+3)
n = 1

What is the total sum of EACH TERMS third decimal digit? If it is a whole 
number, simply add a zero as it will not affect the value. As an example:

1.4378125  2.4932175

7 + 3 = 10

Enter the number in integer format as it will not have any decimals to it.
"""
def fun(n):
    return (3*n+2) / (2*n+3)

sum = 0
for n in xrange(1, 10001):
    term = str(fun( float(n) ))
    if len(term) > 4:
        sum += int(term[4])

print sum