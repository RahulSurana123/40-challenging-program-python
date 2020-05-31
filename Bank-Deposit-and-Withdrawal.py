
def account_info():
    print("\nCurrent Account Information")
    for key, value in bank_account.items():
        print(f"{key.title()}: {value}")
    print()


def transact_now():
    account_type = input("What account would you like to access (Savings / Checking) : ").lower()

    if account_type == 'savings' or account_type == 'checking':
        transact_type = input("What type of transaction would you like to have (deposit / withdrawal) : ").lower()

        if transact_type.lower().startswith('d'):
            money = int(input("How much money : "))
            bank_account[account_type] += money
            print(f"\nDeposited ${money} into {bank_account['name'].title()}'s {account_type} account.")
        elif transact_type.lower().startswith('w'):
            money = int(input("How much money : "))
            if bank_account[account_type] < money:
                print(f"\nYou you have only ${bank_account[account_type]} amount in your this account")
            else:
                bank_account[account_type] -= money
                print(f"\nWithdrawal ${money} from {bank_account['name'].title()}'s {account_type} account.")
        else:
            print("\nplease select correct transaction_type (deposit / withdrawal)")
    else:
        print(f"\nSorry you don't have any {account_type.title()} account.")


print("Welcome to Python First National Bank")
bank_account = {
                "name": input("Hello, what is your name : ").title(),
                "savings": int(input("How much money would you like to open your savings accounts with : ")),
                "checking": int(input("How much money would you like to open your checking accounts with : "))
                }

keep_transacting = True

while keep_transacting:
    account_info()
    transact_now()
    keep_transacting = input("Would you like to make another transaction (y/n) : ").lower() == 'y'

account_info()
