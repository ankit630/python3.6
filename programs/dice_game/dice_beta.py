import random

player = random.randint(1,6)
print("You rolled " + str(player))

ai = random.randint(1,6)
print("The Computer rolled " + str(ai))

if player > ai:
    print("You win")
else:
    print("You loose")
