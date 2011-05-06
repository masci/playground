"""
A pandigital number makes use of the digits 1 through 9 at least once but not 
in any particular order. For example:

146523798  is a 9 digit pandigital

What is the smallest value of k such that 2^k has it's last 9 digits 
pandigital from 1 to 9? (Note: ^ means exponent).

This requires a more clever method to solve as the numbers will get large fast.
"""

def is_pandigital(n):
    n = str(n)
    is_pan = True
    for i in xrange(1,len(n)+1):
        if n.find(str(i)) < 0: 
            is_pan = False
            break
    return is_pan

k=1
while not is_pandigital( str(2**k)[-9:] ):
    k+=1

print k