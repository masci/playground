"""
A classic problem for computer science algorithms is calculating the 
minimum/maximum weight in a triangle of numbers.

Given an input file of a triangle of 50 rows (060.txt), calculate the 
maximum sum in the triangle from the top row to the bottom row.
"""

rows = []
f = open("060.txt", "r")
for l in f:
    rows.append([int(x) for x in l.strip().split(" ")])

costs = {}

def max_cost(row,col):
    if col<0 or col>len(rows[row-1]):
        return 0
    
    if row == 0:
        return rows[0][0]
    
    if (row,col) in costs:
        return costs[(row,col)]
    
    c = max( [max_cost(row-1, col-1), max_cost(row-1, col) ] ) + \
        rows[row][col]
    costs[(row,col)] = c
    return c

res = []
for i in xrange(len(rows[-1])):
    res.append(max_cost(len(rows)-1, i))

print max(res)
