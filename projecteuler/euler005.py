"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
"""

def MCD(a, b):
	while b != 0:
		a, b = b, a % b
	return a
 
def mcm(a, b):
	return a*b/MCD(a, b)

if __name__ == '__main__':
    print reduce(mcm, range(1, 21))
