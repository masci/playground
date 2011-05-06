"""
Given the following information about a US telephone touchtone keypad:

1: (NONE)   2: A,B,C    3: D,E,F
4: G,H,I    5: J,K,L    6: M,N,O
7: P,R,S    8: T,U,V    9: W,X,Y

calculate the product of each characters value.

As an example, say the user enters: "Practice", the product would be:

7 * 7 * 2 * 2 * 8 * 4 * 2 * 3 = 37,632

What is the value of this string: "Programming Challenges are fun"?
"""

lookup = { 'a': 2, 'b': 2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4, 
'j':5, 'k':5, 'l':5, 'm':6, 'n':6, 'o':6, 'p':7, 'r':7, 's':7, 't':8, 'u':8,
'v':8, 'w':9, 'x':9, 'y':9 }

string = str("Programming Challenges are fun").lower().replace(' ', '')

def main():
    print reduce(lambda x, y: x*y, [lookup[x] for x in string])
    
if __name__ == "__main__":
    main()