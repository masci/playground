"""
If there are 3 people in a room, the probability of two of those people having
THE SAME birthday is 0.008. For 4 people, it is 0.016 and for 5 people, it is
0.027.
Using the same rule of at least two people in a room of size 25, what is the
probability (rounded to the nearest 1000th) of two people having THE SAME
BIRTHDAY?
For the purpose of the calendar, there are 365 days in the year (Feb. 29th is
counted a Mar. 1st).
"""
def different_bd(n):
    if n==1: 
        return 1
    else:
        return different_bd(n-1) * (365. - (n-1)) / 365

def main():
    print 1 - different_bd(25)

if __name__ == "__main__":
    main()
