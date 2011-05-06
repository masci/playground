"""
Given an input file of hexadecimal numbers (hex.txt), how many total 
keystrokes are required to spell out all those numbers? (To use a number 
requires only 1 keystroke). Enter your answer in lowercase hexadecimal.

For example, if the total was 1529 strokes, the answer in hexadecimal would 
be: 5f9 (entered as such). 
"""
pads = {
    'a':1,'b':2,'c':3,
    'd':1,'e':2,'f':3,
    'g':1,'h':2,'i':3,
    'j':1,'k':2,'l':3,
    'm':1,'n':2,'o':3,
    'p':1,'q':2,'r':3,'s':4,
    't':1,'u':2,'v':3,
    'w':1,'x':2,'y':3,'z':4,
    '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1
}

def count_strokes(w):
    ret = 0
    for dgt in str(w):
        ret += pads[dgt]
    return ret

count=0
f = open('065.txt', 'r')
for line in f:
    count += count_strokes( line.strip().lower() )

print hex(count)
    