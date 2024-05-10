import random

print("Game Time Baby")


class Player:
    def __init__(self, name): 
        self.name = name # player name 
        self.hand = [] # the cards the player has in their hand.
        

    def draw_card(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.append(card)
            print(f"{self.name} drew: {card.value} of {card.suit}")
    
            return card
        else:
            return None

    def show_hand(self, reveal=False):
        if reveal:
            print(f"{self.name}'s hand:")
            for card in self.hand:
                card.show()
        else:
            print(f"{self.name}'s hand: [Card Hidden, {self.hand[1]}]")

    def get_hand_value(self):
        value = sum([int(card.value) if card.value.isdigit() else (10 if card.value != 'A' else 1) for card in self.hand])
        num_aces = sum([1 for card in self.hand if card.value == 'A'])
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def is_busted(self):
        return self.get_hand_value() > 21

    # def take_turn(self, deck, next_player):
    #     card = self.draw_card(deck)
    #     if card:
    #         print(f"{self.name} drew: {card}")
    #     else: 
    #         print (f"{self.name} tried to draw, but no more cards left")

    #     if deck.cards:
    #         next_player.take_turn(deck, self)
    #     else:
    #         self.show_hand()
    #         next_player.show_hand()
    #         print("The deck is empty. Game over.")


    
    # to find the sum of all the cards
    
    # def who_is_winner(self, player_hand, dealer_hand):
    #     player_value = sum([int(card.value) if card.value.isdigit() else (10 if card.value != 'A' else 1) for card in player_hand])
    #     dealer_value = sum([int(card.value) if card.value.isdigit() else (10 if card.value != 'A' else 1) for card in dealer_hand])

    #     if player_value == dealer_value:
    #         return "Tieeeeeeeeee"
    #     elif player_value > dealer_value:
    #         return "Player wins this game"
    #     else: 
    #         return "Dealer wins this game"
  
        

class Card: 
    suits = ["Hearts",
             "Diamonds",
             "Clubs",
             "Spades"]
    
    values = ["2",
              "3",
              "4",
              "5",
              "6",
              "7",
              "8",
              "9",
              "10",
              "J",
              "Q",
              "K",
              "A"]
    
    def __init__(self, suit, value):
        self.suit = suit #this is for declaring hearts/spades etc 
        self.value = value  # this is for the value on the card, 2, 3, 4, 5, 10, J, Q, K etc
    
    def show(self):
        print ("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self, num_decks=1):
        self.cards = []
        self.num_decks = num_decks
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # self explantory 
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ] # self explantory 
        self.cards = [Card(value, suit)
                      for _ in range(self.num_decks)
                      for suit in suits
                      for value in values]
        
      

    def shuffle_deck(self):
      random.shuffle(self.cards) # random method will randomize a value 

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
 
    # Code for Player, Card, and Deck classes remains the same

deck = Deck(num_decks=1)
deck.shuffle_deck()

player1 = Player(input("Enter Player 1's name: "))
player2 = Player(input("Enter Player 2's name: "))

# Initial deal
player1.draw_card(deck)
player2.draw_card(deck)
player1.draw_card(deck)
player2.draw_card(deck)

# Show initial hands
player1.show_hand()
player2.show_hand()

# Player 1's turn
while not player1.is_busted() and input("Player 1, do you want to draw another card? (y/n): ") == 'y':
    player1.draw_card(deck)
    player1.show_hand()

# Player 2's turn
while not player2.is_busted() and input("Player 2, do you want to draw another card? (y/n): ") == 'y':
    player2.draw_card(deck)
    player2.show_hand()

# Dealer's turn
if not player1.is_busted() and not player2.is_busted():
    dealer = Player("Dealer")
    dealer.draw_card(deck)
    dealer.draw_card(deck)
    dealer.show_hand(reveal=True)
    while dealer.get_hand_value() < 17:
        dealer.draw_card(deck)
        dealer.show_hand(reveal=True)

# Determine winner
player1_value = player1.get_hand_value()
player2_value = player2.get_hand_value()
dealer_value = dealer.get_hand_value() if not player1.is_busted() and not player2.is_busted() else 0

if player1.is_busted() and player2.is_busted():
    print("Both players busted. Dealer wins!")
elif player1.is_busted():
    print("Player 1 busted. Dealer wins!")
elif player2.is_busted():
    print("Player 2 busted. Dealer wins!")
else:
    if dealer_value > player1_value and dealer_value > player2_value:
        print("Dealer wins!")
    elif player1_value > dealer_value and player1_value > player2_value:
        print(f"{player1.name} wins!")
    elif player2_value > dealer_value and player2_value > player1_value:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")


# deck = Deck(num_decks=1)
# deck.shuffle_deck()

    
# player1 = Player(input("Enter Player 1's name: "))
# player2 = Player(input("Enter Player 2's name: "))



# for _ in range(5):
#     player1.draw_card(deck)
#     player2.draw_card(deck)

# player1.show_hand()
# player2.show_hand()

# player1_card = player1.hand[0]
# player2_card = player2.hand[0]

# print("Player 1's card:", player1_card(show))
# print("Player 2's card:", player2_card(show))

# player1_card = Card('suit', 'value') 
# player2_card = Card('suit', 'value')

# winner = player1.who_is_winner(player1.hand, player2.hand)
# print(winner)

# player1.take_turn(deck, player2)
