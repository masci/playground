"""
Given the following number representing a pattern:

2053 = 2^0 + 5^3 = 1 + 125 = 126

Note: ^ means exponent

Look above at the number "20"; in this sequence it represents 2 to the 0 power 
which is 1. The other number "53" represents 5 to the 3rd power which is 125. 
Then final answer is calculated by the sum of each term.

Given this number below:

342345820139586830203845861938475676

What is the answer using the above pattern?
"""

digits = '342345820139586830203845861938475676'
tot = 0
i = 0

while i < len(digits): 
    num = digits[i:i+2]
    tot += int(num[0])**int(num[1])
    i += 2

print tot