import random
print("Welcome to Thesaurus App")
thesaurus = {
    "Amazing": ["Incredible",	"Unbelievable",	"Improbable",	"Astonishing" ],
    "Begin": ["Start",	"Open",	'Launch',	"Initiate"],
    "Crooked": ["Bent",	"Twisted",	"Zigzag",	"Hooked"],
    "Delicious": ["Savory",	"Delectable",	"Appetizing",	"Luscious"],
    "Eager": ["Keen",	"Fervent",	"Enthusiastic",	"Involved"],
}

print("\nChoose a word from the thesaurus and i will give you a synonym")
print("\nHere are the list of words from thesaurus :")

for key in thesaurus.keys():
    print(f"\t - {key}")

key = input("\nWhat word would you like to choose : ").title()
print(f"\nA Synonym of {key} is {thesaurus[key][random.randint(0,3)]}")
decision = input("Would you like to see the whole thesaurus (Yes/No) :").title() == "Yes"
if decision:
    for key, value in thesaurus.items():
        print(f"\n{key} synonym are:")
        for val in value:
            print(f"\t- {val}")
    exit()
print("Hope you enjoyed the program.\t Thank you!")