import random
print("Welcome to game of rock paper scissor")
n = int(input("\nHow many rounds would like to play : "))
options = ["Rock", "Paper", "Scissors"]
score_player = 0
computer_score = 0
for i in range(1, n + 1):
    print(f"\nRound {i}")
    print(f"Player:{score_player}\tComputer:{computer_score}")
    decision = input("Time to pick... Rock, Paper, Scissors: ").title()
    r = random.randint(0, 2)
    com_decision = options[r]
    if not options.__contains__(decision):
        print("\tThat is not a valid game option!")
        print("\tComputer gets the point")
        computer_score += 1
        continue
    print(f"\tComputer: {options[r]}")
    print(f"\tPlayer: {decision}")
    if com_decision == decision:
        print("\tIt is a tie, how boring!")
        print("\tThis round was a tie.")
    if r == 0 and decision == options[1]:
        print("\tPaper covers Rock")
        print("\tYou win this round")
        score_player += 1
    if r == 1 and decision == options[2]:
        print("\tScissors cut Paper")
        print("\tYou win this round")
        score_player += 1
    if r == 2 and decision == options[0]:
        print("\tRock Breaks Scissor")
        print("\tYou win this round")
        score_player += 1
    if r == 1 and decision == options[0]:
        print("\tPaper covers Rock")
        print("\tComputer win this round")
        computer_score += 1
    if r == 2 and decision == options[1]:
        print("\tScissors cut Paper")
        print("\tComputer win this round")
        computer_score += 1
    if r == 0 and decision == options[2]:
        print("\tRock Breaks Scissor")
        print("\tComputer win this round")
        computer_score += 1

print("\nFinal Game Results")
print(f"\t Round Played: {n}")
print(f"\tPlayer Scored: {score_player}")
print(f"\tComputer Scored: {computer_score}")
if computer_score > score_player:
    print("Winner: Computer  :-( ")
if computer_score < score_player:
    print("Winner: Player  :-) ")
if computer_score == score_player:
    print("The game was a tie, Well Played! You were a Tough Competitor.")
