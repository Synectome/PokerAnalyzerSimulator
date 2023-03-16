# take 7 cards and determine the best hand that can be made from 
# at least 1 card from plyr hand, and 3 or 4 cards from the table
# then return a hand rank
import cardDeck as cd
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

def is_straight(player_cards, table_cards):
    rankic = {}
    for card in player_cards:
        rank = cd.get_rank(card)
        if rank in rankic.keys():
            rankic[rank] += 1
        else:
            rankic[rank] = 1
    for card in table_cards:
        rank = cd.get_rank(card)
        if rank in rankic.keys():
            rankic[rank] += 1
        else:
            rankic[rank] = 1
    

"""Returns true if there is a flush involving at least one card of the players hand.
    Does not check for ranking of flush."""
def is_flush(player_cards, table_cards):
    suitic = {}
    for card in player_cards:
        suit = cd.get_suit(card)
        if suit in suitic.keys():
            suitic[suit] += 1
        else:
            suitic[suit] = 1
    for card in table_cards:
        suit = cd.get_suit(card)
        if suit in suitic.keys():
            suitic[suit] += 1
        else:
            suitic[suit] = 1
    for suit, count in suitic.items():
        if count >= 5 and (cd.get_suit(player_cards[0]) == suit or cd.get_suit(player_cards[1]) == suit):
            return True
    return False

    


    