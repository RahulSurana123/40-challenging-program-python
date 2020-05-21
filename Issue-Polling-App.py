print("Welcome to polling App, Your Issue will be solved here.")

issue = input("\nWhat is the yes no issue that we are taking vote for : ")
n = int(input("What is the number of people we are taking vote from :"))
password = input("Enter the password used to see polling data : ")

voters_details = {}
vote_count = {"yes": 0, "no": 0}

for i in range(n):
    voter = input("\nEnter Your Full Name voter :").title()
    print(f"Here is our issue : {issue}")
    if voter in voters_details:
        print("\nSorry, it seems someone with the same name has already voted.")
        continue
    answer = input("What do you think yes or no : ").lower()
    voters_details[voter] = answer
    if answer.startswith("y"):
        vote_count["yes"] += 1
    elif answer.startswith("n"):
        vote_count["no"] += 1
    print(f"\nThank you {voter.title()}! Your vote {answer} has been registered")
print(f"\nThe following {len(voters_details)} people voted :")
for key in voters_details.keys():
    print(key)

print(f"\nFor the following issue : {issue}")

if vote_count["yes"] > vote_count["no"]:
    print(f"yes wins! {vote_count['yes']} votes to {vote_count['no']}")
elif vote_count["yes"] < vote_count["no"]:
    print(f"no wins! {vote_count['no']} votes to {vote_count['yes']}")
else:
    print(f"It was a tie! {vote_count['yes']} votes to {vote_count['no']}")

data_display_permission = input("\nTo see the voting result enter the admin password : ") == password
if data_display_permission:
    for key, value in voters_details.items():
        print(f"Voter: {key}\t Vote: {value}")

print("Thank you for using your Issue Polling App")
