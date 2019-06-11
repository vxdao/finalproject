"""A collection of function for doing my project."""

import random

playing = True
withdraw = False
# defining suits , ranks amd values of the cards 
card_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

#creating card class
class Card:
    
    def __init__(self, suit, rank):
        """
        card_suits: list
        card_ranks: list
        card_value: dictionary 
        
        """
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

# make deck , shuflle and deal fucntions 

class Deck:
    
    def __init__(self):
        """ step to make a Deck """
        self.deck = []
        for suit in card_suits:
            for rank in card_ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        card_deck = ''
        for card in self.deck:
            card_deck = card_deck + '\n' + card.__str__() 
        return 'The deck has\n' + card_deck
            
    def shuffle(self):
        """use random method to shuffle the deck"""
        random.shuffle(self.deck)
        
    def deal(self):
        """use pop method to deal a card"""
        single_card = self.deck.pop()
        return single_card
    
#creating a hand

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0  
        self.aces11 = 0   
    
    def add_card(self,card):
        """ step to add cards """
        self.cards.append(card)
        self.value =self.value + card_values[card.rank]
        if card.rank == 'Ace':
            self.aces11 = self.aces11 + 1
    
    def ace_cases(self):
        """ an Ace can be 11 or 1 """
        while self.value > 21 and self.aces11:
            self.value = self.value - 10
            self.aces11 = self.aces11 - 1
            
# making chips          

class Chips:
    
    def __init__(self):
        self.total = 200  # the player's original money balance 
        self.bet = 0
        
    def win_bet(self): # winning function
        self.total = self.total + self.bet
    
    def lose_bet(self): # losing function
        self.total = self.total - self.bet
    
    def withdraw_bet(self): # withdrawing function
        self.total = (self.total - (self.bet/2))
        
    def push_bet(self):  # pushing function
        self.total = self.total 
        
   
        
# Taking bets

def take_bet(chips):
    """ applying try and Exception to prompt player need to bet the money they have in their balance"""
    while True:
        try:
            chips.bet = int(input('place your bet please  '))
        except ValueError:
            print("Sorry, you need to place an integer money")
        else:
            if chips.bet > chips.total:
                print('Sorry, you can not bet more money than your current balance which is {} '.format(chips.total))
            else:
                break 
                
# game cases scenerios

def player_busts(player,dealer,chips): # player bust
    """step to make a player_busts"""
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips): # player win
    """step to make a player_win"""
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips): # dealer bust
    """step to make a dealer bust"""
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips): # dealer win
    """step to make dealer win"""
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer, chips):   # a push 
    """steps to make a push"""
    print("Dealer and Player tie! It's a push.")
    chips.push_bet()
       
def player_withdraw(player, chips): # player withdraw
    """ steps to make a player withdraw"""
    print("You lost half your betting money!")
    chips.withdraw_bet()
    
    
                    

# making hits

def hit(deck,hand):
    """ step to make a hit call """
    hand.add_card(deck.deal())
    hand.ace_cases()

# making hit or stand or withdraw function

def hit_or_stand_or_withdraw(deck,hand):
    """ step to make the hit_or_stand_or_withdraw function
    parameter: 
    input : deck , hand and player either choose hit , stand or withdraw
    output: the result of choose from hit , stand or withdraw will appear accordingly to the choosen 
    """
    global playing
    global withdraw 
    
    withdraw = False
    playing = True
    
     
    while True:
        x = input("you want to Hit ,Stand ? Enter 'h' for Hit or 's' for Stand or 'w' for withdraw ")
       
        if x[0].lower() =='w':
          
            playing = False 
            withdraw = True
            break
        
        
        elif x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands. now Dealer is playing.")
            playing = False
            
       
        else:
            print("Sorry, please try again. choose either Hit or Stand ")
            continue
        break
    
    if not playing and withdraw:
        return 0 #withdraw
    elif not playing and not withdraw:
        return 1 #stand
    else:
        return 2 #hit


# to display card function

def show_some_card(player,dealer):
    """step to do show card ( hidden 1 card of the dealer)"""
    print("\nDealer's Hand:")
    print("<card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep = '\n')
        
def show_all_card(player,dealer):
    """step to do show all the card """
    print("\nDealer's Hand:", *dealer.cards, sep = "\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep = '\n')
    print("Player's Hand = ", player.value)

    

