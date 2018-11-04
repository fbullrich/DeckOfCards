# Function for shuffling a deck
# Takes an array 'Deck' and randomizes order

import random
random.seed()


#  Example values
# Maindeck = [1, 2, 3, 4, 5]
# shuffle_steps = 5


def shuffling(Maindeck, shuffle_steps):
    # sets a number of steps and creates a new array to be returned
    steps = 0
    Shuffler = Maindeck

    while steps < shuffle_steps:
        # I dont know if this is a good way to shuffle but whatever
        firstR = random.randint(0, len(Maindeck) - 1)
        secondR = random.randint(0, len(Maindeck) - 1)
        
        Shuffler[firstR], Shuffler[secondR] = Shuffler[secondR], Shuffler[firstR]

        steps +=1

    return Shuffler

# #testing
# Shuffled_deck = shuffling(Maindeck, shuffle_steps)
# print(Shuffled_deck)
