"""
Given an input file containing 1000 random blackjack hands between 3 players 
(here: blackjack.txt), calculate the number of blackjacks encountered for any 
player in all games.

A blackjack is defined as an Ace of any suit and a face card (Jack, Queen ,
King) or 10 of any suit.

The input file looks like this: (as an example)

4H 5C AD JH 9C 10H

This means that player one has a 4 of hearts and a 5 of clubs; player 2 has an 
Ace of Diamonds and a Jack of Hearts (which counts as a blackjack); player 3 
has a 9 of Clubs and a 10 of Hearts.

For the purpose of this problem, it is known that there is a standard 52 card 
deck which is reshuffled for each game.
"""

def card_ok(card):
    return (card == '1') or (card == 'J') or (card == 'Q') or (card == 'K') or (card == 'A')

def is_blackjack(hand):
    c1 = hand[0][0]
    c2 = hand[1][0]
    if (c1 != 'A') and (c2 != 'A'): return False
    if c1 == c2: return False
    return card_ok(c1) and card_ok(c2)

def main():
    bj_a = 0
    bj_b = 0
    bj_c = 0
    f = open('016.txt', 'r')
    for line in f:
        hands = [x for x in line.strip().split(' ')]
        if is_blackjack(hands[0:2]): bj_a += 1
        if is_blackjack(hands[2:4]): bj_b += 1
        if is_blackjack(hands[4:6]): bj_c += 1
    print bj_a+bj_b+bj_c

if __name__ == "__main__":
    main()