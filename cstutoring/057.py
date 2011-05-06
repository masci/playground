"""
In probability, there are such things as permutations and combination's. 
A permutation is an ordered arrangement of objects.

For example, there are 6 ways you can arrange the letters in the set 
{a, b, c}:

a b c
a c b
b a c
b c a
c a b
c b a

Using the set of letters {a, b, c, ..., m, n, o}, what is the 
123,456,789th permutation?

NOTE: Enter the answer in ALL LOWERCASE LETTERS without any spaces between 
them. 
"""
import time
try:
    import psyco
    psyco.full()
except ImportError:
    pass

def perm(lst):
    if len(lst) == 1:
        yield lst
    else:
        for p in perm(lst[1:]):
            for i in xrange(len(p)+1):
                yield p[:i] + lst[0:1] + p[i:]

t = time.time()
i=1
for p in perm(range(97,112)):
    if i==123456789:
        print "".join([chr(x) for x in p])
        break
    i+=1
print time.time() - t
        