"""
You are given the following rules about strings:

1. There can only be an even number of vowels.
2. There muse be AT LEAST 3 digits.
3. There must be AT MOST 3 non-alpha numeric characters 
(defined as not in the set {0...9,a...z,A...Z}).
4. There must be NO OCCURRENCE of the letters 'b' or 'q' 
in the string.

Using these above rules, what is the total number of valid strings in the 
input file strings.txt which contains 1000 randomly generated strings?
"""
import re

def count_vowels(s):
    v = ['a','e','i','o','u']
    return len( filter(lambda x: x in v, s) )

def count_digits(s):
    p = re.compile('\d')
    return len( filter(lambda x: p.match(x), s))

def count_nonalpha(s):
    p = re.compile('[^a-zA-Z0-9]')
    return len( filter(lambda x: p.match(x), s))

def is_valid(s):
    s = s.strip()
    return count_vowels(s) % 2 == 0 and count_digits(s) > 2 and \
        count_nonalpha(s) < 4 and not s.count('b') and not s.count('q')

f = open('036.txt', 'r')
print len( filter(is_valid, [x for x in f]) )
