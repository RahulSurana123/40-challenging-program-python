print("Welcome to the Frequency Analysis App")

# for m in range(1, 3):
phrase = '''
Capitol has emerged triumphant from a civil war. Now, with the rebellious Districts quelled, the once-powerful 
Snows live a precarious existence in a penthouse apartment, concealing their poverty from the rest of the city’s 
aristocracy. The Games are in their 10th year, and losing their audience; those in charge decide to bring in 
mentors from the city’s elite to increase engagement. The teenage Coriolanus is chosen to mentor Lucy Gray Baird, 
an eccentric vagabond singer who has been picked as a tribute from District 12. He must guide her to win, pleasing
both the spectators and his teachers. Coriolanus sees his chance to gain glory back for his family name, his eyes
firmly fixed on the cash prize and his future career.
Everything you would expect from Collins is here: fraught teenage love; plenty of violence; character names 
untethered from their contexts (Fabricia Whatnot; Satyria Click) and a pervasive awareness of the power of media. 
Snow and his fellow mentors are always thinking about how they look on screen, how their actions will be judged. 
Nefarious tactics are put into play without question; deaths are barely registered. It is a frightening view of 
adolescence that accepts constant surveillance as a norm. Meanwhile, his teacher, the borderline insane Dr Gaul, 
is conducting genetic experiments. Her relationship with her pupils mirrors that of the mentors and the tributes: 
exploitative, vicious, mercenary.
'''.lower()

character_dict = {}
character_dict2 = {}
for i in range(97, 123):
    c = phrase.count(chr(i))
    character_dict[chr(i)] = c

print(f"\nHere is the frequency analysis from phrase 1 :")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in character_dict.items():
    print(f"\t{key}\t\t{character_dict[key]}\t\t{round(character_dict[key] / sum(character_dict.values()) * 100, 4)}")

sorted_char_list = [k for k in sorted(character_dict.items(), key=lambda kv: kv[1], reverse=True)]
print("\nLetter occurrence from highest to lowest :")
for (i, y) in sorted_char_list:
    print(i, end="")

statement = '''
    Writing on Instagram stories, Bieber denied 6ix9ine’s allegations, stating that if five or more copies of a single
     are purchased on the same credit card, all of those sales are discounted from the song’s chart placing. 
     He stated that Nielsen, the US data company responsible for compiling the Billboard charts, had checked the 
     figures “and found all our sales were legit because our fans are amazing and bought them”.
    Grande, posting on Instagram, responded to 6ix9ine’s allegations without naming him: “to anybody that is displeased 
    with their placement on the chart this week or who is spending their time racking their brain thinking of as many ways 
    as they can to discredit hardworking women (and only the women for some reason.....), i ask u to take a moment to 
    humble yourself.”
    Billboard published a detailed article refuting 6ix9ine’s allegations. “Overall, Stuck With U drew 28.1m US streams, 
    26.3m in radio airplay audience and 108,000 sold in the tracking week … Gooba had 55.3m US streams, 172,000 in radio 
    airplay audience and 24,000 sold. Those sums resulted in the songs’ respective rankings on this week’s Hot 100.”
'''.lower()

for i in range(97, 123):
    c = statement.count(chr(i))
    character_dict2[chr(i)] = c

print(f"\nHere is the frequency analysis from phrase 2 :")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in character_dict2.items():
    print(f"\t{key}\t\t{character_dict2[key]}\t\t{round(character_dict2[key] / sum(character_dict2.values()) * 100, 4)}")

sorted_char_list2 = [k for k in sorted(character_dict2.items(), key=lambda kv: kv[1], reverse=True)]
print("\nLetter occurrence from highest to lowest :")
for (i, y) in sorted_char_list2:
    print(i, end="")

encode_dict = {}
for (i, k), j in zip(sorted_char_list, range(26)):
    encode_dict[i] = sorted_char_list2[j][0]
decode_dict = {}
for (i, k), j in zip(sorted_char_list2, range(26)):
    decode_dict[i] = sorted_char_list[j][0]

# print(decode_dict)
# print(encode_dict)

task = input("\n\nWhat do you want to do with your message encode or decode :").lower() == "encode"
message = input("Enter the message you want to encode or decode : ").lower()
message = message.replace(" ", "")
if task:
    for i in range(len(message)):
        p = message[i]
        print(encode_dict[p], end="")
else:
    for i in range(len(message)):
        p = message[i]
        print(decode_dict[p], end="")
print()