print("Welcome to Vote Registration App")

name = input("\nEnter your name : ").title()
age = int(input("Enter your age : "))
parties = ["Bjp", "Congress", "Siv Sena", "Aap"]
if age < 18:
    print("\nSorry! you are not eligible to vote")
    exit()
print(f"\nCongratulation {name}! you are eligible to vote")
print("\nBelow are mentioned name of all the party you can vote any one of them: ")
for party in parties:
    print(f"\t- {party.upper()}")
choice = input("What party would you like you to choose : ").title()
if choice == "BJP":
    print("Congo you have voted for BJP who is a majority party.")
elif choice.title() in parties:
    print(f"You have voted for {choice} who is not a majority party")
else:
    print(f"{choice} is not in the election")
