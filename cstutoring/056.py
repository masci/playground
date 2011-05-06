"""
The Knights Tour of chess states that a standard knight piece can move 
(or "tour") the board by visiting each square once. There are two types of 
tours, open or closed but for this problem it is not relevant to use this 
terminology.

Recall that a knight moves in L shaped patterns as denoted below:

----------------
|  |X |  | X|  |
|--|--|--|--|--|
|X |  |  |  | X|
|--|--|--|--|--|
|  |  |K |  |  |
|--|--|--|--|--|
|X |  |  |  | X|
|--|--|--|--|--|
|  |X |  | X|  |
----------------

where K is the knight and 
X represents where it may move to.

A tour will begin at the top left square on the board. Here is one possible 
solution on a 5x5 sized board where the numbers indicate the move the knight 
took:

1    16   11   6   3
10   5    2    17  12
15   22   19   4   7
20   9    24   13  18
23   14   21   8   25

Beginning at the top left each time, what is the product of the total number 
of solutions for a 4x5, 4x7 and a 5x5 sized boards? 
"""
import time, copy

moves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))

def pos_ok(board, x, y):
    return (x>=0 and y>=0) and \
        (y<len(board[0]) and x<len(board)) and \
        board[x][y] == 0

def movegen(board, x, y, counter):
    board[x][y] = counter
    if counter == len(board)*len(board[0]):
        yield board
    else:
        for m in moves:
            new_x,new_y = x+m[0], y+m[1]
            if pos_ok(board, new_x, new_y):
                for b in movegen(copy.deepcopy(board), new_x, new_y, counter+1):
                    yield b
    board[x][y] = 0

def print_board(board):
    for line in board:
        print line
    print ""

t1 = time.time()
prod = 1

count = 0
board = [[0 for y in xrange(5)] for x in xrange(4)]
for b in movegen(board, 0, 0, 1):
    count +=1
print "Solutions:%d"%count
prod *= count

count = 0
board = [[0 for y in xrange(7)] for x in xrange(4)]
for b in movegen(board, 0, 0, 1):
    count +=1
print "Solutions:%d"%count
prod *= count

count = 0
board = [[0 for y in xrange(5)] for x in xrange(5)]
for b in movegen(board, 0, 0, 1):
    count +=1
print "Solutions:%d"%count
prod *= count

print "elapsed: ",time.time() - t1
print prod
