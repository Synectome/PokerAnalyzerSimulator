class Player:

    name : int # may not need a name
    c1 : int
    c2 : int
    hand : list
    chips : int
    folded : bool

    def __init__(self, name, chips=1000):
        self.name = name
        self.c1 = None
        self.c2 = None
        # current best hand
        self.hand = []
        self.chips = chips
        self.folded = False