import random


members = ["Mahesh", "Sujal", "Sneha", "Saptarshi"]

leader = random.choice(members)
print(leader)

#exercise:
#write a program for a dice roll using random module
 
def roll_dice():
    return random.randint(1, 6)

print(roll_dice())

class roll_dice:
    def roll(self):
        return random.randint(1, 6)

roll_dice = roll_dice()
print(roll_dice.roll())


