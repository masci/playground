"""
The squares of first 5 positive integers are 1,4,9,16 and 25.

The cubes of first 5 positive integers are 1,8,27,64 and 125.

Consider now the numbers that can be written as the sum of a square and a 
cube. A few examples:

9=1+8=1^2+2^3
12=4+8=2^2+2^3
232=16+216=4^2+6^3

Find the sum of all distinct numbers less than 100,000 that can be written as 
the sum of a square and a cube.
"""
import time

cubes = set()
squares = set()

def fill_sets():
    target = 100000
    i=1
    q=0
    while q < target:
        q = i**2
        squares.add(q)
        c = i**3
        if c<target: cubes.add(i**3)
        i+=1

def check(n):
    for i in cubes:
        if (n-i) in squares: return True
    return False

def main():
    sum = 0
    for x in xrange(1,100001):
        if check(x):
            sum+=x

    print sum

if __name__ == "__main__":
    t1 = time.time()
    fill_sets()
    main()
    t2 = time.time()
    print "time in sec:",(t2-t1)
