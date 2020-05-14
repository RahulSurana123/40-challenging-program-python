print("Welcome to Shipping Accounts Program")

users = ["Rahul", "kruti", "Bill"]
user = input("Hello! please enter your username: ").title()

if not (user in users):
    print("Sorry you do not have account with us. GoodBye!")
    exit()

print("Hello " + user + ". Welcome to your account.")
print("Current shipping prices are as follows:")
print("\nShipping orders 0 to 100: \t\t$5.10 each")
print("Shipping orders 100 to 500: \t\t$5.00 each")
print("Shipping orders 500 to 1000: \t\t$4.95 each")
print("Shipping orders over 1000: \t\t$4.80 each")

n = int(input("How many items would you like to ship : "))
p = 0.0
if n < 100:
    p = 5.10
elif n < 500:
    p = 5.00
elif n < 1000:
    p = 4.95
else:
    p = 4.80


cost = p * n
print(f"To ship {n} items it will cost you ${cost} at ${p} per item.")
decision = input("Would you like to place this order (Y/N): ").startswith("Y")

if decision:
    print(f"Okay. Shipping your {n} items.")
else:
    print("Okay no order is being placed at this time")
