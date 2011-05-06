"""
In math, a Cartesian plane is most commonly known as an X,Y graph. 
This graph has 4 quadrants. Here is the listing for the Quadrants and the 
relation to the (x,y) pair:

Quad. I: (x, y)
Quad. II: (-x, y)
Quad. III: (-x, -y)
Quad. IV: (x, -y)

The pair (3, -5) lies in Quardant IV.
The pair (3, 3) lies in Quard. I

Given an input file of 1000 randomly generated x, y pairs (011.txt), 
how many of those pairs lie in Quadrant III?
"""

def which_quadrant(coord):
    if coord[0] > 0:
        if coord[1] > 0: return 1
        else: return 4
    else:
        if coord[1] > 0: return 2
        else: return 3

def main():
    sum=0
    f = open('011.txt', 'r')
    for line in f:
        if which_quadrant( [int(x) for x in line.strip().split(',')] ) == 3:
            sum+=1
    print sum

if __name__ == "__main__":
    main()