# take 7 cards and determine the best hand that can be made from 
# at least 1 card from plyr hand, and 3 or 4 cards from the table
# then return a hand rank

# hand ranks:
# 1: high card = [hc, 0, (c1, c2, c3, c4, c5)]
# 2: pair = [p, 1, (c1, c2, c3, c4, c5)]
# 3: two pair = [tp, 2, (c1, c2, c3, c4, c5)]
# 4: three of a kind = [tk, 3, (c1, c2, c3, c4, c5)]
# 5: straight = [s, 4, (c1, c2, c3, c4, c5)]
# 6: flush = [f, 5, (c1, c2, c3, c4, c5)]
# 7: full house = [fh, 6, (c1, c2, c3, c4, c5)]
# 8: four of a kind = [fk, 7, (c1, c2, c3, c4, c5)]
# 9: straight flush = [sf, 8, (c1, c2, c3, c4, c5)]
# 10: royal flush = [rf, 9, (c1, c2, c3, c4, c5)]

def hand_value(player_cards, table_cards):
    # check for royal flush
    # check for straight flush
    # check for four of a kind
    # check for full house
    # check for flush
    # check for straight
    # check for three of a kind
    # check for two pair
    # check for pair
    # check for high card
    pass

def straight():
    # check for straight
    # if straight, return True
    # else return False
    pass

def flush():
    # check for flush
    # if flush, return True
    # else return False
    pass