"""
In math, a midpoint is a point lying between two (x, y) coordinates on a graph.

As an example, say we have the points:
(2, 5)
(4, 10)

The midpoint is found by adding the two x coordinates, the two y coordinates 
and dividing by 2. The result is another (x, y) pair:

((2+4)/2 , (5+10)/2)

The answer is: (3, 7.5)

Given an input file of 100 pairs of (x,y) coordinates (plane22.txt), what is 
the sum of ALL the resulting y coordinates values?
"""
def main():
    sum_y = 0.0
    f = open('022.txt', 'r')
    for line in f:
        points = line.strip().split('|')
        y_a = float(points[0].split(',')[1])
        y_b = float(points[1].split(',')[1])
        sum_y += (y_a + y_b)/2
    print sum_y

if __name__ == "__main__":
    main()