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
# 6: flush = [f, 5, (c1, c2, c3, c4, c5)]                 -function complete
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

"""Returns True, [card1, card2, card3, card4, card5] for the best straight available,
or False, None if no straight is available"""
def is_straight(player_cards, table_cards):
    rankic = {}
    cardic = {}
    for card in player_cards:
        rank = cd.get_rank(card)
        if rank in rankic.keys():
            rankic[rank] += 1
            cardic[rank].append(card)
        else:
            rankic[rank] = 1
            cardic[rank] = [card]
    for card in table_cards:
        rank = cd.get_rank(card)
        if rank in rankic.keys():
            rankic[rank] += 1
            cardic[rank].append(card)
        else:
            rankic[rank] = 1
            cardic[rank] = [card]
    
    ranked = rankic.keys().sort()
    # are there 5 sequential cards?
    count = 0
    seq = []
    # max is number of sequential cards, 2,3,4,5,6,7,8 between 5 and 7, it will be 0 if less than 5
    max = 0
    # maxseq is the actual list of cards that are allowed. may be nested list if multiple of same rank.
    maxseq = []
    for i in range(len(ranked) - 1):
        seq.append()
        if ranked[i] + 1 != ranked[i + 1]:
            seq = [cardic[ranked[i]]]
            count = 0
            continue
        if count >= 5:
            max = count
            maxseq = [card for card in seq] # copy the list
    # if not, return False, None
    if max == 0:
        return False, None
    
    # if there are exactly 5 sequential cards, ensure that at least one of them is in the players hand
    if max == 5 and 
    # if not, return False, None
    

"""Returns True, [card1, card2, card3, card4, card5] for the best flush available,
otherwise returns False, None"""
def is_flush(player_cards, table_cards):
    suitic = {}
    cardic = {}
    # populate dictionaries with cards
    for card in player_cards:
        suit = cd.get_suit(card)
        if suit in suitic.keys():
            suitic[suit] += 1
            cardic[suit].append(card)
        else:
            suitic[suit] = 1
            cardic[suit] = [card]
    for card in table_cards:
        suit = cd.get_suit(card)
        if suit in suitic.keys():
            suitic[suit] += 1
            cardic[suit].append(card)
        else:
            suitic[suit] = 1
            cardic[suit] = [card]

    # possible flush suit
    suit = max(suitic)
    # return if no flush
    if suitic[suit] < 5:
        return False, None

    # if there are 5 cards to make a flush and at least one is in the players hand, we return the 5 cards
    if suitic[suit] == 5 and (cd.get_suit(player_cards[0]) == suit or cd.get_suit(player_cards[1]) == suit):
        return True, cardic[suit]
    # more than 5 cards in the flush, guarantees that the player has at least one card of the correct suit,
    # but we need to return the highest 5 cards THAT ALSO contains at least one of the players cards
    # Example:
        # Player has 2h, 3h
        # Table has 4h, 5h, 8h, 9h, 10h
        # over all highest = 4h, 5h, 8h, 9h, 10h, but is invalid because it does not contain the players cards
        # highest valid = 3h, 5h, 8h, 9h, 10h

    # we have suitic[suit] > 5, so we need to find the highest 5 cards that contain at least one of the players cards
    highest = highest_ranking_x(cardic[suit], 5)
    # the players cards are in the highest possible flush, so we return em.
    if (cd.get_suit(player_cards[0]) in highest or cd.get_suit(player_cards[1]) in highest):
        return True, highest
    # if there are 5 cards in the flush on the table, all higher than the players card, we have a problem
    else:
        # player cards are both flush suited
        if cd.are_suited(player_cards[0], player_cards[1]):
            # of the player cards, choose the highest one of the flush suit
            highest_player_card = player_cards[0] if player_cards[0] > player_cards[1] else player_cards[1]
        else:
            # only one of the players cards are flush suited
            highest_player_card = player_cards[0] if cd.get_suit(player_cards[0]) == suit else player_cards[1]
        flush_hand = [highest_player_card] + highest_ranking_x(cardic[suit], 4)
        return True, flush_hand


"""Returns the highest ranking x cards regardless of suit"""
def highest_ranking_x(cards, x):
    cards_as_ranks = [cd.get_rank(card) for card in cards]
    cards_as_ranks.sort()
    while len(cards_as_ranks) > x:
        cards_as_ranks.pop(0)
    return [cd.rank_plus_suit_to_card(rank, cd.get_suit(cards[0])) for rank in cards_as_ranks]

    