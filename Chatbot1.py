print("Hello! I am AI Bot. What's your Name? : ")

name=input()

print(f"Nice to Meet you, {name}!")

print("How are you Feeling Today ? (good/bad) : ")
mood=input().lower()

if mood=="good":
    print("I'm glad to hear that!")
elif mood=="bad":
    print("I'm sorry to hear that. Hope things get better soon")
else:
    print("I see. Sometimes it's hard to put feelings into words")

print(f"It was a nice chatting with you {name}. Goodbye!")