from random import *

def guess_random_number(tries, start, stop):
    num = randint(int(start), int(stop))

    while tries != 0:
        print(f"number of tries remaining {tries}")

        guess = int(input(f"Guess a number between {start} and {stop}: "))

        if guess == num:
            print("You guessed the correct number!")
            return

        elif guess < num:
            print("Guess higher!")
            

        elif guess > num:
            print("Guess lower!")

        tries -= 1
    print(f"You have failed to guess the number: {num}")

guess_random_number(5, 0, 10)



def guess_random_num_linear(tries, start, stop):
    num = randint(int(start), int(stop))

    for x in range(len(start, stop)):
        
