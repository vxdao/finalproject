"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

from my_module.functions import *


#  play game function 

while True:

        print("Welcome to my Blackjack game.")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips()

        # ask Player to place their betting money 
        take_bet(player_chips)

        # Show cards (keep one dealer card hidden)
        show_some_card(player_hand, dealer_hand)


        withdraw = False
        playing = True
        while playing:  



            # ask for Player to Hit or Stand or Withdraw
            result = hit_or_stand_or_withdraw(deck, player_hand)
            
            if result == 0: #withdraw
                playing = False
                withdraw = True
            elif result == 1: #stand 
                playing = False
            else:
                playing = True # hit
            

            # Show cards (but keep one dealer card hidden)
            show_some_card(player_hand,dealer_hand)

            # if player withdraw
            if withdraw:
                player_withdraw(player_hand, player_chips)
                break 


            # If player's hand exceeds 21, run player_busts() and break out of loop

            if player_hand.value >21:
                player_busts(player_hand, dealer_hand, player_chips)
                break



        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21 and withdraw == False:


            while dealer_hand.value <17:
                hit(deck, dealer_hand)


            show_all_card(player_hand,dealer_hand)

            # winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value == player_hand.value:
                push(player_hand, dealer_hand, player_chips)


        # Inform Player of their chips total
        print("Your new balance is ", player_chips.total)

        # Ask to play again
        new_game = input(" you want to play again? Enter 'y' for yes  or 'n' for no")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('thank you for playing , see you again')

            break





