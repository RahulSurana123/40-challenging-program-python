import matplotlib.pyplot as plt
def loan_info_display(loan_dict, counts):
    print(f"\n-------- Loan Information after {counts} months --------")
    for key, value in loan_dict.items():
        print(f"{key.title()}: {value}")


print("Welcome To Loan Calculator App")
loan_detail = {
                "principal": float(input("Enter the loan amount : ")),
                "rate": float(input("Enter the interest rate : ")),
                "monthly payment": float(input("Enter the desired monthly payment amount : ")),
                "money paid": 0
               }
prinipal_records = []
count = 0
prinipal_records.append(loan_detail["principal"])
loan_info_display(loan_detail, count)
input("Press 'Enter' to begin paying off your loan.")

while not loan_detail["principal"] <= 0:
    principal = loan_detail["principal"]

    interest = principal * (loan_detail["rate"] / 12) / 100
    if principal + interest < loan_detail["monthly payment"]:
        loan_detail["principal"] = 0
        loan_detail["money paid"] += (principal + interest)
        prinipal_records.append(principal)
    else:
        loan_detail["principal"] += (interest - loan_detail["monthly payment"])
        loan_detail["money paid"] += loan_detail["monthly payment"]
        prinipal_records.append(principal)
    count += 1
    loan_info_display(loan_detail, count)
    if loan_detail["principal"] >= principal:
        print(f"You will never be able to pay debt off with this Monthly Payment!!" +
              f"\nmonthly payment:${loan_detail['monthly payment']} is less than interest amount: ${interest}")
        exit()
print(f"\nCongratulation! You Paid off your loan in {count} months")
print(f"Your initial loan was ${prinipal_records[0]} at a rate of {loan_detail['rate']}%")
print(f"Your monthly payment as ${loan_detail['monthly payment']}")
print(f"You spent ${loan_detail['money paid']} in total")
print(f"You spent ${loan_detail['money paid'] - prinipal_records[0]} on interest!")
month = list(range(0, count + 1))
plt.plot(month, prinipal_records)
plt.xlabel("Month Number")
plt.ylabel("Principal of Loan")
plt.title(f"{loan_detail['rate']}% Interest With ${loan_detail['monthly payment']} Monthly Payment")
plt.show()
