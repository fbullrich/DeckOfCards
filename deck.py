from enum import Enum
import numpy

# values for the deck. May want to change things to allow
# for values to be passed through cmd line

num_suits = 4
cards_per_suit = 10
face_suits = 3
jokers = True
num_jokers = 2

# Create a number of suits up to 4 suits, more could be added

# S - spades, H - hearts
# C - clubs, D - diamonds
Suits = ['S', 'H', 'C', 'D']

total_suits = []    

for i in (0, num_suits):
    # Create an array of numbers from 1 to cards per suit
    basic_cards = numpy.arange(1, cards_per_suit + 1)

    # Create an array of symbols that indicate suit
    suited_cards = [Suits[i]] * cards_per_suit

    # join both arrays to create an array of squential numbers
    # plus a corresponding symbol
    for x in (0, cards_per_suit):
        suited_cards[x] = suited_cards[x] + str(basic_cards[x])
    total_suits.append((suited_cards))

print(total_suits)

    