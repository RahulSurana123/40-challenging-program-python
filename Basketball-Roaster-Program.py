print("Welcome to Basketball Roaster Program\n")
players = []
players.append(input("Who is your point guard: ").title())
players.append(input("Who is your shooting guard: ").title())
players.append(input("Who is your small forward: ").title())
players.append(input("Who is your power forward: ").title())
players.append(input("Who is your center: ").title())
print("\n\t Your Starting 5 for the upcoming basketball season ")
print("\t\tPoint Guard : " + players[0])
print("\t\tShooting Guard : " + players[1])
print("\t\tSmall Forward : " + players[2])
print("\t\tPower Forward : " + players[3])
print("\t\tCenter : " + players[4])
injured = players.pop(2)
print("Oh no! , " + injured + " is injured")
print("Your roaster has only " + str(len(players)) + " players in it")
players.insert(2, input("Who will take " + injured + "'s spot: ").title())
print("\n\t Your Starting 5 for the upcoming basketball season ")
print("\t\tPoint Guard : " + players[0])
print("\t\tShooting Guard : " + players[1])
print("\t\tSmall Forward : " + players[2])
print("\t\tPower Forward : " + players[3])
print("\t\tCenter : " + players[4])
print("\nGood Luck " + players[2] + " you will do great")
print("Your Roaster has " + str(len(players)) + " players")