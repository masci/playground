"""
Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

data = [int(x) for x in """
75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 
63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 
16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 
91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 
31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".strip().split(" ")]

rows = []
last=0
for i in xrange(1,16):
    rows.append( data[last:i+last] )
    last+=i

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
