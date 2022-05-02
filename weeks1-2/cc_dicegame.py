import random

high_score = 0

def dice_game():
    global high_score

    while True:
        roll = input(f"Current High Score: {high_score}\n1) Roll Dice\n2) Leave Game\nEnter your choice: ")
        if roll == "1":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
           
            previous_high = high_score
            high_score = max(high_score, dice1 + dice2)

            print(f"\nYou roll a... {dice1}\nYou roll a... {dice2}\n\nYou have rolled a total of: {dice1 + dice2}\n")
            if high_score == dice1 + dice2 and high_score != previous_high:
                print("New high score!\n")
        elif roll == "2":
            print("Goodbye!")
            break
        else:
            print("Please enter 1 or 2\n")

dice_game()
