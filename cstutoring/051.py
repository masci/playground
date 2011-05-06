from itertools import permutations

def how_many_pos(n):
    count = 0
    cols = range(n)
    for vec in permutations(cols):
        if (n == len(set(vec[i]+i for i in cols)) 
        == len(set(vec[i]-i for i in cols))):
            count += 1
    return count

res = 1
for i in xrange(4,11):
    res *= how_many_pos(i)

print res
