import random
import time

player = random.randint(1,6)
print("You rolled " + str(player))

ai = random.randint(1,6)
print("The computer rolls.....")
time.sleep(2)
print("The Computer rolled " + str(ai))

if player > ai:
    print("You win")
elif player == ai:
    print("Tie game.")
else:
    print("You loose")
