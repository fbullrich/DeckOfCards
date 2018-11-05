import numpy as np

# values for the deck. May want to change things to allow
# for values to be passed through cmd line

num_suits = 4
cards_per_suit = 10
num_face_cards = 3
jokers = True
num_jokers = 2

# Create a number of suits up to 4 suits, more could be added

# S - spades, H - hearts
# C - clubs,  D - diamonds
Suits = ['S', 'H', 'C', 'D']
suitTranslation = {
    'S':'of Spades',
    'H':'of Hearts',
    'C':'of Clubs',
    'D':'of Diamonds',
}

# 3 face cards - might replace 1 with ace but thats work
Face_cards = ['Jack', 'Queen', 'King']

total_deck = []    

for i in range(num_suits):
    # Create an array of numbers from 1 to cards per suit
    basic_cards = np.arange(1, cards_per_suit + 1)

    # Create an array of symbols that indicate suit
    suited_cards = [Suits[i]] * cards_per_suit

    # join both arrays to create an array of squential numbers
    # plus a corresponding symbol
    for x in range(cards_per_suit):
        suited_cards[x] = (suited_cards[x] + str(basic_cards[x]))
        total_deck.append(suited_cards[x])

    suited_faces = [Suits[i]] * num_face_cards
    for x in range(num_face_cards):
        suited_faces[x] = suited_faces[x] + Face_cards[x]
        total_deck.append(suited_faces[x])   

if jokers:
    for x in range(num_jokers):
        total_deck.append('j')

# # for testing
# print(total_deck)

    
