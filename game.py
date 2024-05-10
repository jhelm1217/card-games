import time, random

print("Hello, Play my mini Game please")
player_name = input("What's your name: ")


#This class is used to intilize the players name, score, and the bet amount
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bet = 0

#I'm defining a score variable and increasing it by 1.
    def increase_score(self):
        self.score += 1

#I'm setting the bet to a number value
    def place_bet(self, amount):
        self.bet = amount

 # Reset bet back to 0? I think it works. idk...lol   
    def reset_bet(self):
        self.bet = 0

# establishing that there are two players. one player is a real person and the other is a robottt
player = Player(player_name)
computer = Player("Computer")

# this is my card valuess, the rank, suits and the deck
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = []


# this is looping over each card in the deck and assigning a suit, rank and number value to each card.
value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1


#shuffle the deck, of course. had to import it at the top 
random.shuffle(deck)
# score = 0
# card1 = deck.pop(0)

# was trying to get the game to continue until somebody reaches 5 points, but when I added in bets
#it messed everything up, need to fix this buggggg
while player.score >= 0 and computer.score >= 0:
    print("Start Round!)")
# using a Try/Except method?
#this code part ios allowing a person to set a bet for a number between 1 and 10. 
#they have to enter a correct number or it wont work. 
    while True: 
        try: 
            bet_amount = int(input("Place your bet (1-10): "))
            if 1 <= bet_amount <= 10:
                player.place_bet(bet_amount)
                break
            else:
                print("Enter number between 1 and 10.")
        except ValueError: 
            print("Please enter a valid number.")

# if the deck is not empty, reshuffle
    if not deck:
        print("Reshuffling deck...")
        random.shuffle(deck)  

#prints out each players score.
    print("Your score so far is", player.score)
    card1 = deck.pop()
    print("\n\nThe current card is", card1[0])

# this is a loop for the game, guessing a high or low number
#i 
    while True:
        choice = input("higher or lower?") # this is what your choices are.
        if len(choice) > 0: # you have to enter something 
            if choice[0].lower() in ["h","l"]: # you have to enter h or l, Im useing Lower so i dont have to capitalize the inputs.
                break
        
#Card1 and Card2 are from two different decks but they are used in the game to determine which card is the highest 
#or lowest 
    card2 = deck.pop(0) #pop is used to show to first element in the array. 
    print("The next card picked is", card2[0])
    time.sleep(1)

#Game begins
#real peerson goes first 
    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Correct!")
        player.increase_score()
        player.score += player.bet 
        time.sleep(1)
    elif choice[0].lower() == "h" and card2[1] < card1[1]:
        print("Wrong!, you've lost some money", player.bet)
        player.score -= player.bet
        player.reset_bet()
        time.sleep(1)
        break
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Correct!")
        player.increase_score()
        player.score += player.bet 
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("Wrong!, you've lost some money", player.bet)
        player.reset_bet()
        time.sleep(1)
        
    else:
        print("draw!")

    #Computers Turn
computer_choice = random.choice(["h", "l"]) # Computer guesses randomly too 
print("\nComputer's choice:", computer_choice)
time.sleep(1)

card2 = deck.pop(0)
print("The next card picked is", card2[0])
time.sleep(1)

if computer_choice == "h" and card2[1] > card1[1]:
        print("Computer is correct!")
        computer.increase_score()
        computer.score *= player.bet
        time.sleep(1)
elif computer_choice == "h" and card2[1] < card1[1]:
        print("Computer is wrong!")
        computer.reset_bet()
        time.sleep(1)
elif computer_choice == "l" and card2[1] < card1[1]:
        print("Computer is correct!")
        computer.increase_score()
        computer.score *= player.bet
        time.sleep(1)
elif computer_choice == "l" and card2[1] > card1[1]:
        print("Computer is wrong!")
        computer.reset_bet()
        time.sleep(1)
        # break
"""else:
        print("Draw!")"""
card1 = card2

"""print("Game over!")
"""
if player.score == 20:
    print("You win")
else: 
    print("Computer wins")

print("You final score is", player.score)
print("Computer's final score is", computer.score)

print("Game over!")

time.sleep(4)

#game_ended = False
#while not game_ended:
    # Player's turn
    # ...

    # Computer's turn
    # ...

    # Check if the player wants to quit or has run out of money/score
    #if player_wants_to_quit_condition or player.score <= 0: # You'll need to define player_wants_to_quit_condition
        #print("Game ended. Thank you for playing!")
        #game_ended = True
    #elif other_end_condition: # Define other conditions for ending the game
        #print("Game ended. [Reason for ending]")
        #game_ended = True