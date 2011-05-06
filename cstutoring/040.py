"""
By the famous binomial theorem, we can develop Pascal's Triangle. Here is the 
first 5 rows of the famous triangle:

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
......

A few things to observe; the first and last numbers of each row is 1. To 
calculate the other numbers, it is simply the sum of the above numbers to the 
left and right.

Let's just say that we wanted to keep it short and sweet. For the sake of 
being lazy, we will mod the triangle by 100 to only observe numbers no larger 
than 99 in the triangle. The triangle above is still the same even when 
modding it by 100. The reason for the mod is due to the fact that the numbers 
get large really fast!

What is the sum of the sums of the first 25,000 rows of Pascal's "Modded" 
Triangle?
"""
import time

def gen_mod_triangle(limit):
    row = []
    prev = []
    index = 1
    while index <= limit:
        if not len(prev): 
            prev = row = [1]
        else:
            row = [1]
            for i,x in enumerate(prev):
                if i == len(prev)-1: break
                row.append( (x+prev[i+1])%100 )
            row.append(1)
            prev = row
        yield row
        index += 1

t = time.time()
tot=0
for x in gen_mod_triangle(25000):
    tot += sum(x)
print tot
print time.time() - t
