# Function for shuffling a deck
# Takes an array 'Deck' and randomizes order

import random
random.seed()


# Example values
# maindeck = [1, 2, 3, 4, 5]
# shuffle_steps = 5


def shuffling(maindeck, shuffle_steps):

    for i in range(len(maindeck)):
        j = random.randint(i, len(maindeck) -1)
        
        maindeck[i], maindeck[j] = maindeck[j], maindeck[i]

    return maindeck

#testing
# for x in range (2):
#     Shuffled_deck = shuffling(maindeck, shuffle_steps)
# print(Shuffled_deck)
