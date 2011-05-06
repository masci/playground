"""
Someone in an office tower often wondered where an elevator car ended the day, 
seeing as how it always begins on the first floor.

To answer this question, a programmer decided to keep track of the direction 
of the elevator. A positive number meant that it was going up while a negative 
number meant that it was going down.

Given the input file of directions (elevator.txt), on what floor did the 
elevator finish the day. For this problem, you are to begin at the first 
floor (1). The office tower is also 100 floors and 10 basements 
(meaning -10 <= floor <= 100) for a total of 110 floors.

Enter the floor below. If it is negative, enter the minus sign as well.
"""

floor = 1
f = open('033.txt', 'r')
for line in f:
    floor += int(line.strip())

print floor
