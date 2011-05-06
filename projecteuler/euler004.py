""" Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n):
	# please notice the pythonic syntax to reverse the string using list comprehension!
	nstr = '%d' % n
	return nstr[::-1] == nstr
	
def check():
	res = 0
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			prod = i*j
			if isPalindrome(prod) and prod > res:
				res = prod
	return res

if __name__ == '__main__':
	print check()