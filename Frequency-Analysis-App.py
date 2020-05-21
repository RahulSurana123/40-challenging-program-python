print("Welcome to the Frequency Analysis App")

for m in range(1, 3):
    phrase = input("\nEnter the word or phrase to count occurrence of each letter :").lower()
    character_dict = {}

    for i in range(97, 123):
        c = phrase.count(chr(i))
        if c != 0:
            character_dict[chr(i)] = c

    print(f"\nHere is the frequency analysis from phrase {m} :")
    print("\n\tLetter\t\tOccurrence\tPercentage")
    for key, value in character_dict.items():
        print(f"\t{key}\t\t{character_dict[key]}\t\t{round(character_dict[key] / sum(character_dict.values()) * 100, 4)}")

    sorted_char_list = [k for k in sorted(character_dict.items(), key=lambda kv: kv[1], reverse=True)]
    print("\nLetter occurrence from highest to lowest :")
    for (i, y) in sorted_char_list:
        print(i, end="")
    print("")
print("Thank you for using Frequency Analysis App")
