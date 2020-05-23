import random
print("Welcome to Guess the word App")

words = {"Sports": ["football", "soccer", "basketball", "baseball", "tennis"],
         "Fruit": ["banana", "apple", "mango", "watermelon", "grape"],
         "color": ["black", "purple", "red", "orange", "grey", "yellow"],
         "animal": ["elephant", "tiger", "hippo", "giraffe"],
         "birds": ["hen", "crow", "sparrow", "penguin"]
         }

keys_list = list(words.keys())
flag_play_again = True
while flag_play_again:
    category = random.randint(0, len(keys_list) - 1)
    topic = random.randint(0, len(words[keys_list[category]]) - 1)

    dashed_solution = ""
    real_solution = words[keys_list[category]][topic]
    game_going_on = True
    letter_revealed = []
    for i in range(len(real_solution)):
        dashed_solution += "-"
    # letter_revealed.append(i)
    print(f"\nGuess a {len(real_solution)} letter word from the following category: {keys_list[category]}")
    print(dashed_solution)
    k = 1
    guess = ""
    while game_going_on:
        if not dashed_solution == real_solution and not guess == real_solution:
            guess = input("\nEnter your guess: ")
        if guess == real_solution or dashed_solution == real_solution:
            if guess == real_solution:
                print(f"That is correct. you guessed {real_solution} in {k} turns")
            if dashed_solution == real_solution:
                print("You have lost the game, Better luck next time ")
            flag_play_again = input("Would you like to play again (y/n): ") == 'y'
            game_going_on = False
            k = 1
        else:
            print("That is not correct.  Let us reveal a letter to help you!")
            reveller = random.randint(0, len(real_solution) - 1)
            while reveller in letter_revealed:
                reveller = random.randint(0, len(real_solution) - 1)
            letter_revealed.append(reveller)
            dashed_solution = ""
            for i in range(len(real_solution)):
                if i not in letter_revealed:
                    dashed_solution += "-"
                else:
                    dashed_solution += real_solution[i]
            print(dashed_solution)
        k += 1
