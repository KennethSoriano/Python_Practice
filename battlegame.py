
while True:
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    dragon = "Dragon"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dragon_hp = 300

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dragon_damage = 50

    print("1)Wizard: hp=70 damage=150 \n2)Elf: hp=100 damage=100 \n3)Human: hp=150 damage=20") 
    character = input("Choose your character")


    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break

    if character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break

    if character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    if (character < "1" or character > "3"):
        print("Unknown character")
    if (character != wizard or character != elf or character !=human):
        print("Unknown character")

        
print(f'You have chosen the character: {character}\nHealth: {my_hp} \nDamage: {my_damage}') 

while True: 
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's current hitpoints is", dragon_hp)

    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print("You have been damaged by the Dragon! Your current hit points are:", my_hp)

    if my_hp <= 0:
        print(character, "has lost the battle.")
        break