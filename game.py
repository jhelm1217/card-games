import time, random

print("Hello, Play my mini Game please")
player_name = input("What's your name: ")

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bet = 0

    def increase_score(self):
        self.score += 1

    def place_bet(self, amount):
        self.bet = amount
    
    def reset_bet(self):
        self.bet = 0

player = Player(player_name)
computer = Player("Computer")

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1

random.shuffle(deck)
# score = 0
# card1 = deck.pop(0)


while player.score < 5 and computer.score < 5:
    print("Start Round!)")
# using a Try/Except method?
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

    if not deck:
        print("Reshuffling deck...")
        random.shuffle(deck)  

    print("Your score so far is", player.score)
    card1 = deck.pop()
    print("\n\nThe current card is", card1[0])


    while True:
        choice = input("higher or lower?")
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
        

    card2 = deck.pop(0)
    print("The next card picked is", card2[0])
    time.sleep(1)


    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Correct!")
        player.increase_score()
        player.score *= player.bet
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
        player.score *= player.bet
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("Wrong!, you've lost some money", player.bet)
        player.reset_bet()
        time.sleep(1)
        break
    else:
        print("draw!")

    #Computers Turn

computer_choice = "h" if card2[1] < 7 else "l"  # Computer guesses based on the card value
print("\nComputer's choice:", computer_choice)
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
else:
        print("Draw!")


card1 = card2

print("Game over!")

if player.score == 5:
    print("You win")
else: 
    print("Computer wins")

print("You final score is", player.score)
print("Computer's final score is", computer.score)

time.sleep(4)
 