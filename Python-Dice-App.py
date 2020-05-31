import random


def random_generation(possibility=1):
    out = random.randint(1, possibility)
    print(f"\t{out}")
    return out


print("Welcome to Python Dice App")

keep_playing = True

while keep_playing:
    n = int(input("\nHow many sides would you like on your dice : "))
    times_to_roll = int(input("How many time do you want to roll dice : "))

    print(f"\nYou rolled {times_to_roll} {n} sided dice")
    print("\n------------- Results are as followed ------------")

    number_on_dice = []

    for i in range(times_to_roll):
        number_on_dice.append(random_generation(n))
    print(f"Total value of your roll is {sum(number_on_dice)} ")

    keep_playing = input("\nWould like to play again (y/n): ").lower() == 'y'

print("Thank you for using python dice app")
