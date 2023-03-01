import cardDeck
import random
import csv
import datetime


class Player:

    name : int # may not need a name
    c1 : int
    c2 : int
    hand : list

    def __init__(self, name):
        self.name = name
        self.c1 = None
        self.c2 = None
        # current best hand
        self.hand = []


def empiracle_shuffle_test_2csv(run_count: int):
    storage = []
    for i in range(run_count):
        deck = cardDeck.deck()
        random.shuffle(deck)
        storage.append(deck)
    with open("PokerAnalyzerSimulator\SimulationData\empiracle_shuffle_test_"+
              str(datetime.datetime.now().strftime("D-%d-%m-%Y_T-%H-%M-%S"))+
              ".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(run_count):
            writer.writerow(storage[i])


def empiracle_shuffle_test_counter(run_count: int):
    # build a dictionary to store the count of each card 
    # in the top position of the deck after shuffling
    countic = {}
    for i in cardDeck.deck():
        countic[i] = 0

    for i in range(run_count):
        deck = cardDeck.deck()
        random.shuffle(deck)
        countic[deck[0]] += 1

    # print the results raw
    print(countic)

    # print the results as deviation from perfect
    for k, v in countic.items():
        print("card: " + str(k) + " deviation: " + str(v - (run_count/52)))
    
    # check if it is a normal distribution
    with open("PokerAnalyzerSimulator\SimulationData\shuffle_count_test_"+
            str(datetime.datetime.now().strftime("D-%d-%m-%Y_T-%H-%M-%S"))+
            ".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for k,v in countic.items():
            writer.writerow([k,v - (run_count/52)])


def start_game(num_players: int):

    # check if the number of players is valid
    if num_players < 2:
        raise ValueError("Must have at least 2 players")
    elif num_players > 9:
        raise ValueError("Cannot have more than 9 players")
    
    players = []
    # create the players
    for i in range(num_players):
        players.append(Player(i))

    # generate the deck and shuffle it
    deck = cardDeck.deck()
    random.shuffle(deck)
    print(deck)

# start_game(2)
empiracle_shuffle_test_counter(10000)