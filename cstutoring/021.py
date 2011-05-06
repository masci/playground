"""
Given an input file of 500 decimal numbers (decimalsB.txt), how many times IN 
TOTAL does the letter D appear when each number is converted into hexadecimal 
format?
"""
def main():
    f = open('021.txt', 'r')
    d=0
    
    for line in f:
        d += hex(int(line.strip())).count('d')

    print d,'D\'s'

if __name__ == "__main__":
    main()