"""
A happy number is built by adding the squares of its digits. Doing this 
permanently, the numbers will end in 1 or 4.

If a positive integer ends with 1, then it is a happy number.

The first few happy prime numbers are:

7, 13, 19, 23, 31, 79, 97, 103, 109 ...

What is the sum of the first 10,000 happy prime numbers?
"""
import time
ish = __import__("062")
isp = __import__("032")

x=1
res=[]
t1=time.time()
while len(res) < 10000:
    if ish.is_happy(x) and isp.isprime(x): res.append(x)
    x+=1

print "time:",time.time()-t1
print sum(res)
