"""
A simple exponent may be 210 which evaluates to 1024. It is an easy one to 
find by any standards and it is easy to see that the sum of the digits is 7. 
However, something like the expression 74719 is much more difficult to find 
and is out of range for most calculators. It evaluates to the 55 digits 
answer below:

3918243614405834507168379223316086523420389920823019283

The sum of those digits is 225.

Given an input file (exponents.txt) and whose lines appear in the format:

747,19

the base appears on the left and 
the exponent appears on the right.

what is the sum of the digits of the largest valued number in the file when 
raising the base to the exponent?
"""
import time

numbers = {}
max_pow = 0

t1 = time.time()

f = open('054.txt', 'r')
for l in f:
    t = [int(x) for x in l.strip().split(',')]
    if t[0]>1 and numbers.setdefault(t[0], 0) < t[1]:
        numbers[t[0]] = t[1]

for k,v in numbers.iteritems():
    try:
        if v<= numbers[k+1]: continue
    except:
        pass
    r = k**v
    if r>max_pow: max_pow = r

print sum(int(x) for x in str(max_pow))
t2 = time.time()-t1
print "elapsed time: %f" % t2