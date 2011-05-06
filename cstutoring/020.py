"""
In computers, everything is represented by 1s and 0s. This is called a binary 
number.

As an example, the integer 5 is represented in binary form by 101. This means, 
working from right to left:

1*2^0 + 0*2^1 + 1*2^2 = 1+0+4 = 5

Given an input file (decimals.txt) of 500 integers, how many 1s IN TOTAL 
appear in the file in each numbers binary representation?

Say you had the numbers 5, 7 and 10

5 = 101
7 = 111
10 = 1010

Total number of 1s: 7
"""
import math

def main():
    f = open('020.txt', 'r')
    ones=0
    
    for line in f:
        number = int(line.strip())
        while number:
            ones += number % 2
            number /= 2
        #for i in xrange( int(math.log(number,2)) + 1 ):
        #    if number & (1<<i): ones+=1

    print ones,'1\'s'

if __name__ == "__main__":
    main()