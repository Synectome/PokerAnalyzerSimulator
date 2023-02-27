spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# generates all of the cards in a deck
def deck():
    deck = []
    for i in range(10):
        deck.append(str(i+1)+"-S")
        deck.append(str(i+1)+"-H")
        deck.append(str(i+1)+"-D")
        deck.append(str(i+1)+"-C")
    for i in ["J", "Q", "K"]:
        for j in ["S", "H", "D", "C"]:
            deck.append(i+"-S")
            deck.append(i+"-H")
            deck.append(i+"-D")
            deck.append(i+"-C")
    return deck


def get_suit(c: str) -> str:
    return c[-1:]


def are_suited(c1: str, c2: str) -> bool:
    return get_suit(c1) == get_suit(c2)