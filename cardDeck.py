
# 1 = 2, 2= 3, 3 = 4, 4 = 5, 5 = 6, 6 = 7, 7 = 8, 8 = 9, 9 = 10, 10 = J, 11 = Q, 12 = K, 13 = A

# generates all of the cards in a deck
def deck():
    return [i+1 for i in range(52)]
    

@staticmethod
def get_suit(c: int) -> str:
    if c < 14:
        return "S"
    elif c < 27:
        return "H"
    elif c < 40:
        return "D"
    else:
        return "C"

@staticmethod
def are_suited(c1: str, c2: str) -> bool:
    return get_suit(c1) == get_suit(c2)

@staticmethod
def get_rank(c: int) -> int:
    return c % 13

@staticmethod
def human_representation(c: int) -> str:
    rank = get_rank(c)
    suit = get_suit(c)
    if rank == 0:
        return "A" + suit
    elif rank < 9:
        return str(rank + 1) + suit
    elif rank == 9:
        return "T" + suit
    elif rank == 10:
        return "J" + suit
    elif rank == 11:
        return "Q" + suit
    elif rank == 12:
        return "K" + suit
    else:
        raise ValueError("Invalid card : {}", c)

@staticmethod
def rank_plus_suit_to_card(rank, suit):
    if suit == "S":
        pass
    elif suit == "H":
        rank += 13
    elif suit == "D":
        rank += 26
    elif suit == "C":
        rank += 39
    else:
        raise ValueError("Invalid suit: {}", suit)
    return rank