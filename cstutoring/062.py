"""
A happy number is built by adding the squares of its digits. Doing this 
permanently, the numbers will end in 1 or 4.

If a positive integer ends with 1, then it is a happy number.

The first few happy numbers are:

1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68.

An example from above is:

13 = 1^2 + 3^2 = 1+9 = 10
10 = 1^2 + 0^2 = 1+0 = 1

How many positive happy numbers are there less than 300,000? 
"""
import time

def is_happy(n):
    digits = [int(x) for x in str(n)]
    res = sum(x**2 for x in digits)
    if res == 1:
        return True
    if res == 4:
        return False
    return is_happy(res)

def main():
    res=[]
    t1=time.time()
    for x in xrange(1,300000):
        if is_happy(x): res.append(x)

    print "time:",time.time()-t1
    print len(res)

if __name__ == "__main__":
    main()
