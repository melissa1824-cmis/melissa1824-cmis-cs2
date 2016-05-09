import random
#Eat at a French restaurant if you are hungry. You have the choice between snails and foie gras. If you are not hunry, you will leave.

def hunger(decision):
	if decision == "yes":
		print "Welcome to Le Boudoir! We have two exquisite items on the menu today!"
		choice = raw_input("Choose True or False to determine what you will eat: ")
		food(choice)
	elif decision =="no":
		print "That's too bad."

def food(decision2):
	if decision2 == "True":
		print "Wait a moment please; Your escargots will be out of the oven sizzling with butter in a few minutes."
	elif decision2 == "False":
		print "Your foie gras will be ready in at least 5 minutes!" 
	
		
def drink(drinkoption):
	if drinkoption == "yes":
		print "We have surprise drinks today."
	elif drinkoption == "no":
		print "That's too bad."

def drinkchoice(surprise):
    surprise = int(raw_input("Choose a number between 1 and 10: "))
    if surprise > random.randint(1, 10):
        print "You chose champagne!"
    else: 
        print "You chose wine!"
    
def main():
    decision1 = raw_input("Are you hungry?: ")
    hunger(decision1)
    decision3 = raw_input("Would u like something to drink?: ")
    drink(decision3)
    drinkchoice(surprise)
    surprise = int(raw_input("Choose a number between 1 and 10: "))
main()
