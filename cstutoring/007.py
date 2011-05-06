"""
Given the following function:

       4^x + x^3 + x^2 + x - 2^x
f(x) = -------------------------
                 3^x

What is the first 3 digits of the value of f(50)?
"""
import time

def f(x):
    return (4**x + x**3 + x**2 + x - 2**x) / (3.**x)

t1 = time.time()
r = str(f(50))
t2 = time.time()
print r[:3],(t2-t1)*1000