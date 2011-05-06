"""
The cross problem states that you can place the numbers 1 through N inside the cross such that no two adjacent cells in any direction (up, down, left or right) contain adjacent numbers (+ or - 1).

Given the shape of an 8 sized cross below where the numbers represent the cell index:

  1 4
0 2 5 7
  3 6


there are only 4 solutions for an 8 sized cross. In the above structure, 
cell 2 is adjacent to cells 0, 1, 3, 4, 5 and 6 while cell 1 is adjacent to 
cell 0, 2, 4 and 5. Here is one of the 4 solutions:

  5 3
2 8 1 7
  6 4


How many solutions are there on a 12 sized cross given the indexes below?

  2 6
0 3 7 10
1 4 8 11
  5 9

"""
from time import time
import psyco
psyco.full()

cross_adj = [
    [1,2,3,4], #0
    [3,4,5], #1
    [3,6,7], #2
    [4,6,7,8], #3
    [5,7,8,9], #4
    [8,9], #5
    [7,10], #6
    [8,10,11], #7
    [9,10,11], #8
    [11], #9
    [11], #10
    [], #11
]

def check_cross(cross):
    i = len(cross)-1
    for cell in cross[::-1]:
        for adj in cross_adj[i]:
            if adj >= len(cross): break
            if abs(cross[adj]-cell) == 1:
                return False
        i-=1
    return True

def gen_cross(cross, values):
    if not len(values):
        yield cross
    else:
        for i,v in enumerate(values):
            next_cross = cross + [v]
            if check_cross(next_cross):
                next_values = values[:i] + values[i+1:]
                for c in gen_cross(next_cross, next_values):
                    yield c

t = time()

cross = []
count=0

for c in gen_cross(cross, range(1,13)):
    count+=1

print "elapsed time: %f sec" % (time() - t)
print "Total count: %d" % count
