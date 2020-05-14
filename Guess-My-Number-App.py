import random
print("Welcome to Guess My Number App")

name = input("\nWhat is your name ? ").title()
print(f"Well {name} i am guessing a number between 1 to 20.")

number = random.randint(1, 20)
for i in range(5):
    guess = int(input("Take a Guess : "))
    if guess == number:
        print(f"Good Job, {name}! you guessed my number in {i + 1} guesses!!")
        exit()
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
print("\nGame Over the number i guesses was " + str(number))