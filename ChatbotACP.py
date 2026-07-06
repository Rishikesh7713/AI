print("Hello! I am AI Bot Made by Rishikesh. What's your Name? : ")

name=input()

print(f"Glad to Meet you, {name}!")

print("Are you Feeling good Today ? (yes/no) : ")
ans=input().lower()

if ans=="yes":
    print("I'm glad to hear that!")
elif ans=="no":
    print("I'm sorry to hear that. Hope things get better soon")
else:
    print("I see. Sometimes it's hard to put feelings into words")

print(f"It was a nice talk with you {name}. Goodbye {name}!")