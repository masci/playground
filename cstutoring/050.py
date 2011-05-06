"""

In honor of our 50th problem, what is the sum of the first 50 terms in the 
sequence given below?

50 100 5000 100 150 ......

Note that you are seeing the first 5 terms.

+50*50/50+50...
"""
def fiftyseq(limit):
    i=50
    count=0
    yield i
    while count < limit:
        if count%3 == 0:
            i+=50
        elif count%3 == 1:
            i*=50
        elif count%3 == 2:
            i/=50
        yield i
        count += 1

print sum(x for x in fiftyseq(49))