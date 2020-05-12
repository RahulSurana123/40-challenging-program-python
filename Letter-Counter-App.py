print("Welcome to the Letter Counter App")

name = input("What is your name:")
print("Hello " + name.title() + "!")
print("I will count the number of times that a specific letter occurs in a message.")

message = input("Please enter a message:")
character = input("Which letter would you like to count the occurrence of:")
print(name.title() + ", your message has " + str(message.lower().count(character)) + " " + character + "'s in it")