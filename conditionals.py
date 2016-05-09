import random
import math
#My game will be like Monopoly. You choose a city from the list for yourself and your opponent. Each city has a different value (random value generated = how much the city is worth in dollars). After choosing a city, a tax value is subtracted from the value of the city. This tax value is randomly generated. If the final value you have is higher than the opponent's, you win. If not, you lose. *** Happiness of citizens is important. *** 

def player1City():
    player1City = raw_input("Which city do you choose?: ")
    if player1City == "Washington":
        value = int('100,000,000')
    elif player1City == "New York":
        value = int('90,000,000')
    elif city == "San Francisco": 
        value = int('80,000,000')
    elif city == "Houston":
        value = int('70,000,000')
    elif city == "Los Angeles":
        value = int('60,000,000')
    elif city == "Las Vegas":
        value = int('50,000,000')
    elif city == "Detroit":
        value = int('40,000,000')
    elif city == "New Orleans":
        value = int('30,000,000')
    elif city == "San Jose":
        value = int('20,000,000')
    elif city == "Philadelphia":
        value = int('10,000,000')
    else:
        value = random.randint((10,000,000), (100,000,000))
    return value

def player2City():
    player2City = raw_input("Which city does player 2 choose?: ")
    if city == "Washington":
        value = int('100,000,000')
    if city == "New York":
        value = int('90,000,000')
    elif city == "San Francisco": 
          value = int('80,000,000')
    elif city == "Houston":
          value = int('70,000,000')
    elif city == "Los Angeles":
          value = int('60,000,000')
    elif city == "Las Vegas":
          value = int('50,000,000')
    elif city == "Detroit":
            value = int('40,000,000')
    elif city == "New Orleans":
          value = int('30,000,000')
    elif city == "San Jose":
          value = int('20,000,000')
    elif city == "Philadelphia":
          value = int('10,000,000')
    else:
          value = random.randint((10,000,000), (100,000,000))
    return value

def taxValue1():
    tax1 = random.randint(5000, 25000)
    taxValue1 = float(tax1/2)
    return

def taxValue2():
    tax2 = random.randint(5000, 25000)
    taxValue2 = float(tax1/2)

def player1specs():
    tax1 = random.randint(5000, 25000)
    taxValue1 = float(tax1/2)
    return player1City
    return taxValue1

def player2specs():
    tax2 = random.randint(5000, 25000)
    taxValue2 = tax2/2
    return player2City
    return taxValue2

def cashbattle(player1City, taxValue1, player2City, taxValue2):
    aftertax1 = int(player1City) - int(taxValue1)
    aftertax2 = int(player2City) - int(taxValue2)
    return aftertax1
    return aftertax2

def result(aftertax1, aftertax2):
    if aftertax1 > aftertax2:
        print "Player 1 WON!"
    else:
        print "Player 2 WON!"

def main():
    player1City = raw_input("Which city do you choose?: ")
    player2City = raw_input("Which city does player 2 choose?: ")
    player1specs()
    player2specs()
    cashbattle(player1City, taxValue1, player2City, taxValue2)
    result()

main()
