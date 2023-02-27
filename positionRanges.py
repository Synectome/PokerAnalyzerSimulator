range = [["AAo", "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s"],
            ["AKo", "KKo", "KQs", "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"],
            ["AQo", "KQo", "QQo", "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s", "Q3s", "Q2s"],
            ["AJo", "KJo", "QJo", "JJo", "JTs", "J9s", "J8s", "J7s", "J6s", "J5s", "J4s", "J3s", "J2s"],
            ["ATo", "KTo", "QTo", "JTo", "TTo", "T9s", "T8s", "T7s", "T6s", "T5s", "T4s", "T3s", "T2s"],
            ["A9o", "K9o", "Q9o", "J9o", "T9o", "99o", "98s", "97s", "96s", "95s", "94s", "93s", "92s"],
            ["A8o", "K8o", "Q8o", "J8o", "T8o", "98o", "88o", "87s", "86s", "85s", "84s", "83s", "82s"],
            ["A7o", "K7o", "Q7o", "J7o", "T7o", "97o", "87o", "77o", "76s", "75s", "74s", "73s", "72s"],
            ["A6o", "K6o", "Q6o", "J6o", "T6o", "96o", "86o", "76s", "66o", "65s", "64s", "63s", "62s"],
            ["A5o", "K5o", "Q5o", "J5o", "T5o", "95o", "85o", "75s", "65s", "55o", "54s", "53s", "52s"],
            ["A4o", "K4o", "Q4o", "J4o", "T4o", "94o", "84o", "74s", "64s", "54o", "44o", "43s", "42s"],
            ["A3o", "K3o", "Q3o", "J3o", "T3o", "93o", "83o", "73s", "63s", "53o", "43o", "33o", "32s"],
            ["A2o", "K2o", "Q2o", "J2o", "T2o", "92o", "82o", "72s", "62s", "52o", "42o", "32o", "22o"]]


class PreFlopRange:
    # default range populated with zeros
    all_ranges = {"utg":[[0]*13]*13, "utg+1": [[0]*13]*13,}
    bet_types = ["fold", "limp", "raise", "raise as bluff"]

    positions = ["utg", "utg+1", "utg+2", "Lojack", "Hijack", "Cutoff", "Button", "Small Blind", "Big Blind"]
    states = ["rfi", "facing rfi", "rfi vs 3bet"]
    adversary_position: str
    position: str
    state: str

    def __init__(self, new_pos: str, new_state: str):
        self.position = new_pos
        print("new Range position : " + self.position)
        self.state = new_state
        print("new Range state : " + self.state)

    @staticmethod
    def valid_position(position):
        if position in PreFlopRange.posisitions:
            return True
        return False

    def choose_range(self):
        # based on the position at the table, and the state
        pass

    def load_range_csv(self):
        pass


