import random
print("------------------------- Power-ball Simulation -----------------------------")

white_balls = int(input("How many number of white-balls to draw from, for 5 winning balls (Normally 69) : "))
if white_balls < 5:
    white_balls = 5
red_balls = int(input("How many number of red-balls to draw from, for 1 winning balls (Normally 26) : "))
if red_balls < 1:
    red_balls = 1
# winning_chances = 1
odds = 1
for i in range(5):
    odds *= (white_balls - i)
odds *= red_balls / 120
# odds = int(odds)
continue_buying = True
print(f"you have a 1 in {odds} chances of winning this lottery.")
n = int(input("Purchase Ticket in what interval : "))
print("\n------------------- Welcome to the Power-ball ----------------------")
winning_ticket = []
white_balls_list = []
red_ball_list = random.randint(1, red_balls)
for i in range(5):
    ball = random.randint(1, white_balls)
    while ball in white_balls_list:
        ball = random.randint(1, white_balls)
    white_balls_list.append(ball)
    winning_ticket.append(ball)
winning_ticket.sort()
winning_ticket.append(red_ball_list)
print(f"\nTonight's winning number are:", end=" ")
for i in white_balls_list:
    print(i, end=" ")
print(red_ball_list)
input("Press 'Enter' to begin purchasing of tickets!!!")
ticket_list = []
ticket_bought = 0
while continue_buying:
    ticket = []
    for i in range(5):
        ball = random.randint(1, white_balls)
        while ball in ticket:
            ball = random.randint(1, white_balls)
        ticket.append(ball)
    ticket.sort()
    ticket.append(random.randint(1, red_balls))
    while ticket in ticket_list:
        print("Losing ticket generated, discarding")
        ticket = []
        for i in range(5):
            ball = random.randint(1, white_balls)
            while ball in ticket:
                ball = random.randint(1, white_balls)
            ticket.append(ball)
        ticket.sort()
        ticket.append(random.randint(1, red_balls))
    ticket_list.append(ticket)
    ticket_bought += 1
    if ticket == winning_ticket:
        print("\nwinning ticket numbers : ", end="")
        for i in winning_ticket:
            print(i, end=" ")
        continue_buying = False
        print(f"\nPurchased a total of {ticket_bought} tickets.")
    else:
        print(ticket)
    if ticket_bought % n == 0:
        print(f"\n{ticket_bought} tickets purchased so far with no winners...")
        continue_buying = input("Keep purchasing tickets (y/n) : ") == 'y'
