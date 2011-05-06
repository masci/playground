"""
Given an input file of 3000 random dice throws, (here: dice.txt) calculate how 
many doubles were rolled.

It is known for this problem that each die are fair in that they are labeled 
with the numbers 1,2,3,4,5 and 6. It is also known that a double is defined as
both dice showing the same number after they are rolled.
"""

def is_double(th):
    return (th[0] == th[1])

def main():
    doubles=0
    f = open('015.txt', 'r')
    for line in f:
        if is_double( [int(x) for x in line.strip().split(' ')] ):
            doubles+=1
    print doubles

if __name__ == "__main__":
    main()