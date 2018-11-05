from deck import *
from shuffle import shuffling
import copy

gameState = True

def valueCalc(card):
    if card == 'j':
        return('Joker!', 15)
    else:
        suit = card[0]
        val = card[1:]

        strVal = val
        # check if val is a face card
        if val == 'King':
            val = cards_per_suit + 3
        elif val =='Queen':
            val = cards_per_suit + 2
        elif val == 'Jack':
            val = cards_per_suit + 1
        else:
            val = int(val)
            
        
        cardDeclaration = ' '.join([strVal, suitTranslation[suit]])
        return(cardDeclaration, val)

while gameState:
    input("Welcome to War! Press any key to continue... \n")

    game_deck = copy.deepcopy(total_deck)
    game_deck = shuffling(game_deck, 500)

    while gameState and len(game_deck) > 1:
        print("Both players draw a card...")

        playerCard = game_deck.pop(0)
        opponentCard = game_deck.pop(0)

        playerDrawn, playerVal = valueCalc(playerCard)
        opponentDrawn, opponentVal = valueCalc(opponentCard)

        input("Ready to reveal? ...\n")

        print("Your card: ", playerDrawn)
        print("My card: ", opponentDrawn)

        if playerVal == opponentVal:
            print("Tie! Nobody wins.")
        elif playerVal > opponentVal:
            print("Congratulations! You have won.")
        else:
            print("Unfortunately, you have lost.")

        keep_playing = input("Play again? (y/n) \n")
        if keep_playing is not ('y' or 'Y'):
           gameState = False

    gameState = False
    
    if len(game_deck) < 2:
        print("No cards left!")
        keepPlaying = input("Play again? (y/n) \n")
        if keepPlaying is ('y' or 'Y'):
            gameState = True
    






