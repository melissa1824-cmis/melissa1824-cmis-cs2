import random
#Eat at a French restaurant if you are hungry. You have the choice between snails and foie gras. If you are not hunry, you will leave.

def getready(outfit):
    print "Let's get ready for dinner! Choose something to wear!"
    if outfit == "Parrot":
        print "You chose blue colored dress pants and a bright yellow suit."
    elif outfit == "Robin":
        print "You're wearing all red."
    else:
        outfit == "Parrot"
        print "You're going to dinner in a clown costume."

def footwear(shoes):
    if shoes == "Brazil":
        print "You chose high heels."
    elif shoes == "Canada":
        print "You chose loafers."
    else:
        shoes == "Thailand"
        print "You chose flip flops."
    
def hunger(decision):
    if decision == "yes":
        print "Welcome to Le Boudoir! We have two exquisite items on the menu today! We will not show you the menu."
        choice = raw_input("Choose True or False to determine what you will eat: ")
        food(choice)
    else:
        decision =="no"
        print "That's too bad."

def food(decision2):
    if decision2 == "True":
        print "Wait a moment please; Your escargots will be out of the oven sizzling with butter in a few minutes."
    else:
        decision2 == "False"
        print "Your foie gras will be ready in at least 5 minutes!" 
	
		
def drink(drinkoption):
    if drinkoption == "yes":
        print "We have surprise drinks today."
    else:
        drinkoption == "no"
        print "That's too bad."

def drinkchoice(surprise):
    if surprise > random.randint(1, 10):
        print "You chose champagne!"
    else: 
        print "You chose wine!"

def output(outfit, shoes):
    return """
You have chosen to wear the {} outfit and shoes from {}.
Hello valued customer!
You have blindly chosen your meal!
Bon appetit!
""".format(outfit, shoes)

def main():
    outfit = raw_input("Choose one of these birds to determine your outfit 'Peacock, Robin, Parrot': ")
    getready(outfit)
    shoes = raw_input("Choose one of these countries to determine your footwear 'Brazil, Canada, Thailand': ")
    footwear(shoes)
    decision = raw_input("Are you hungry?: ")
    hunger(decision)
    decision3 = raw_input("Would u like something to drink?: ")
    drink(decision3)
    surprise = int(raw_input("Choose a number between 1 and 10: "))
    drinkchoice(surprise)
    print output(outfit, shoes) 
main()
