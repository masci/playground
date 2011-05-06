"""
Given a numerical pattern below:

1^2 + 2^3 + 3^4 + 4^5 + .... + 19 ^ 20

What is the last last 5 digits of this pattern?
"""

print str(sum(x**(x+1) for x in xrange(20)))[-5:]