"""
The set of numbers raised to the 10th power is: {1, 1024, 59049, 1048576, 
9765625, .... }

What we want to accomplish is when summing the digits of an element of the 
set, we want to keep summing until we arrive at a single digit answer. We can 
observe that the sum of the digits of 2^10 is 1+0+2+4 = 7. Therefore, we will 
say the number arrives at 7.

We also observe that the sum of the digits of 4^10 is 
1+0+4+8+5+7+6 = 31 = 3+1 = 4. Here, we say the number arrives at 4 after 
summing the digits of the answer until we arrived at the single digit.

Using the rule of summing the digits until you arrive at a single digit, 
how many of the first 10,000 numbers to the 10th power arrive at 4? (Note, you
 are seeing the first number arriving at 4 which is 4^10).
"""

def good_arrival(x):
    res = 0
    x = str(x)
    while len(x) > 1:
        for d in x:
            res += int(d)
        x = str(res)
        if res == 4: return True
        res = 0
    return False

print len ( [x for x in xrange(1, 10001) if good_arrival(x**10)] )
