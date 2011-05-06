"""
Most (NOT ALL) Cell phone keypads look like this (the letters are above the 
respective number):

[NONE]	ABC	DEF
1	2	3

GHI	JKL	MNO
4	5	6

PQRS	TUV	WXYZ
7	8	9

	[SPACE]
	0	

For the word "stop", there are a total of 9 keystrokes needed to spell the 
word. You need to press #7 4 times, #8 once, #6 3 times and #7 once to get it.

For the purpose of this problem, just know that there is no punctuation marks,
 numbers or white spaces and the text message would consist of just 1 word.

Given a text file of over 20000 common English words (words.txt) and using 
the above keypad, how many words have their total number of keystrokes equal 
to a Fibonacci number? 
"""
f = __import__("013")

pads = {
    'a':1,'b':2,'c':3,
    'd':1,'e':2,'f':3,
    'g':1,'h':2,'i':3,
    'j':1,'k':2,'l':3,
    'm':1,'n':2,'o':3,
    'p':1,'q':2,'r':3,'s':4,
    't':1,'u':2,'v':3,
    'w':1,'x':2,'y':3,'z':4
}

def count_strokes(w):
    ret = 0
    for dgt in str(w):
        ret += pads[dgt]
    return ret

fibo = []
for x in f.fiborange(100):
    fibo.append(x)

count=0
f = open('064.txt', 'r')
for line in f:
    strokes = count_strokes( line.strip().lower() )
    if strokes in fibo: count+=1

print count
    