import random

RPS=["rock","paper","scissers"]
i=input("your playing rock paper scissers, pick your champion: ")
ai=random.choice(RPS)
print(ai)
if i == "rock":
    if ai==i:
        print("tie")
    elif ai =="paper":
        print("lose")
    else:
        print("WIN!!!!")
elif i =="paper":
    if ai==i:
        print("tie")
    elif ai =="scissers":
        print("lose")
    else:
        print("WIN!!!!!")
elif i =="scissers":
    if ai==i:
        print("tie")
    elif ai=="rock":
        print("lose")
    else:
        print("WIINN!!!!!")
else:
    print("why you put that? thats not even remotly close to what we told you to put in. try again you loser.")