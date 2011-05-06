"""
Given the Triangle of primes.

2    
3 5   
7 11 13  
17 19 23 29   
31 37 41 43 47   
53 59 61 67 71 73 
....

The sum of the 6th row is 384. Give the sum of the 100th row.
"""
p = __import__("008")
triangle = [x for x in p.build_primes(5050)]
print sum(triangle[-100:])
