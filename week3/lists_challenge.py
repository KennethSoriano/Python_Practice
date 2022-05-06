import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    card = input("Enter any key to pick a card or press Q to quit")
    if card == "Q":
        break
    else:
        card == random.choice(diamonds)
        diamonds.remove(card)
        hand.append(card)
        print(diamonds)
        print(hand)

if not diamonds:
    print("There are no more cards to pick.")
