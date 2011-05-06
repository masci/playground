""" Add all the natural numbers below one thousand that are multiples of 3 or 5.
"""

# list comprehensions are cool!
print sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])