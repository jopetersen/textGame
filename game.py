# a simple text adventure game
import random
print("Hello, let's play a game!")
char_name=input("What is your name? ")

print("Hi "+char_name)
#char_class=input("Do you want to play a warrior, a mage, or a healer?")

# initialize_character
class Character():
    def __init__ (self):
        self.name=char_name
        self.health = 10
        self.strength = 10

#print(health) - fails because health is nested under class

#initialize enemy
class Enemy():
    def __init__ (self):
        self.name = "Baddy"
        self.health = 8
        self.strength = 5

new_enemy = Enemy()

fight =input("A wild enemy has appeared! Fight? (Y/N)" ).upper()

"""
#tests to make sure that the input is correctly parsed
if fight == "Y":
    print("You have chosen to fight")
elif fight == "N":
    print("You have chosen to run away")
else:
    print ("try again")
"""

if fight == "Y":
    def fight (method):
        if method == "sword":
            print("You take a swipe at the enemy with your sword!")
            damage = random.randint(0,5)
            enemy_health=new_enemy.health
            enemy_health= enemy_health-damage
            print("You do " + str(damage) + " damage to your opponent! They now have "
            + str(enemy_health) + " left!")
            #if enemy_health > 0:
    elif fight == "N":
        print("You run away:")
    else:
        print("Working")
