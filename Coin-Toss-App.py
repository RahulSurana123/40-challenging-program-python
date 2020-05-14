import random
print("Welcome to Coin Toss App")

print("\nI will flip the coin a certain number of times")
n = int(input("How many times do you want me to flip the coin : "))

head_count = 0
tail_count = 0
decision = input("Would you like to see each individual result (Y/N) :").upper().startswith("Y")
for i in range(1, n + 1):
    r = random.random()
    if r < 0.5 :
        if decision:
            print("Head")
        head_count += 1
    else:
        if decision:
            print("Tail")
        tail_count += 1
    if head_count == tail_count and decision:
        print(f"At {i} flips , Head and tail count where equal at {head_count} each")

print(f"\nResult of flipping a coin {n} no of times are : ")
print("\nSide\tCount\tPercentage")
print(f"Head\t{head_count}/{n}\t{head_count/n}")
print(f"Tail\t{tail_count}/{n}\t{tail_count/n}")
