"""
A binary clock is a clock which displays sexagesimal time (military format) in 
a binary format. There are also two kinds of representations for a binary 
clock; vertical or horizontal.

Below is the horizontal representation of the time 10:37:49

(H) 0 0 1 0 1 0 (10) 
(M) 1 0 0 1 0 1 (37)
(S) 1 1 0 0 0 1 (49)

so when it is grouped together as a binary string, it looks like this:

001010 100101 110001

Find the total number of 1s in the representations of military time for a full 
24 hour period which elapses from 00:00:00 to 23:59:59. How many total 1s 
appear for the entire year (a regular 365 day year)?
"""
import time

def ones_in(number):
    ones = 0
    while number:
        ones += number % 2
        number /= 2
    return ones

if __name__ == "__main__":
    ones = 0
    for h in xrange(0,24):
        for m in xrange(0,60):
            for s in xrange(0,60):
                ones += ones_in(h) + ones_in(m) + ones_in(s)
    
    print ones * 365