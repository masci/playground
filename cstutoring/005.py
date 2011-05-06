"""
Given the following information:

a = 26, b = 25, c = 24, d = 23 ..... x = 3, y = 2, z = 1

What is the sum of each letter of this sentence: 
"The quick brown fox jumped over the cow"? 
(Note, a white space has no value).
"""

lookup = dict( zip( (chr(x) for x in xrange(97,123)), (x for x in xrange(26,0,-1))) )

s = str("The quick brown fox jumped over the cow").lower().replace(' ','')

def main():
    print sum(lookup[x] for x in s)

if __name__ == "__main__":
    main()

