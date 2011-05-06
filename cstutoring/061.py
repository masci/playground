"""
We know that the set of odd numbers begins as {1,3,5,7,9...}.

We know that the set of prime numbers begins as {2,3,5,7,11,...}.

We know that the set of Fibonacci numbers begins as {1,1,2,3,5,8,...}.

So far, as an example, the intersection of the start of the 3 sets evaluates 
to the set {3, 5} and the sum of the elements is 8.

Given the 3 sets above, each of size 2000, what is the sum of the elements 
in the intersection of all 3 sets? 
"""

m = __import__("008")
f = __import__("013")

odds = set(x for x in xrange(1,4000,2))
primes = set(x for x in m.build_primes(2000))
fibo = set()
fgen = f.fiborange(10**500)
for x in xrange(2001):
    fibo.add(fgen.next())

res = odds.intersection(primes & fibo)
print sum(res)