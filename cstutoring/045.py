"""
Given the following formulas below for generating triangle, pentagonal and 
hexagonal numbers:

Triangle(n) = n(n+1)/2
Pentagonal(n) = n(3n-1)/2
Hexagonal(n) = n(2n-1)

What is the product of the total number of triangle, pentagonal and hexagonal 
numbers appearing in the input file binary.txt when each number is converted 
to decimal?
"""
import string

t=[]
n=x=1
while x < 5000:
    x = n*(n+1)/2
    t.append(x)
    n+=1

p=[]
n=x=1
while x < 5000:
    x = n*(3*n-1)/2
    p.append(x)
    n+=1

h=[]
n=x=1
while x < 5000:
    x = n*(2*n-1)
    h.append(x)
    n+=1

f = open("045.txt", 'r')
nt=np=nh=0
for line in f:
    n = string.atoi(line.strip(), 2)
    if n in t: nt+=1
    if n in p: np+=1
    if n in h: nh+=1

print nt*np*nh