print("Welcome to Database Admin Program")

login_info = {
    "Rahul": "rahul211",
    "Vibey": "same2u3000",
    "K2": "piano123",
    "Adminbabu": "atmanirbhar",
    }

username = input("\nEnter the username : ").title()

if username in login_info.keys():
    password = input("Enter the password : ")
    if login_info[username] == password :
        print(f"\nHello {username}!  You are logged in!")
        if username == "Adminbabu":
            print("\nHere is  the current user database:")
            for key, value in login_info.items():
                print(f"\tUsername: {key} --> Password: {value}")
        else:
            decision = input("Would you like to change your password: ").title().startswith("Y")
            if decision:
                new_password = input("What would you like your new password to be: ")
                if len(new_password) < 8:
                    print(f"{new_password} does not have minimum eight character.")
                else:
                    login_info[username] = new_password
                print(f"\n{username} your password is {login_info[username]}")
            else:
                print("\nThank you, Goodbye!")
    else:
        print("\nIncorrect Password!")
else:
    print("\nSorry you are not a user")
