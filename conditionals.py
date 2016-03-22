import random

#My game will be like Monopoly. You choose a city from the list for yourself and your opponent. Each city has a different value (random value generated = how much the city is worth in dollars). After choosing a city, a tax value is subtracted from the value of the city. This tax value is randomly generated. If the final value you have is higher than the opponent's, you win. If not, you lose. *** Happiness of people is important. *** 

def value(city):
    if city == "Washington":
        value = int(100,000,000)
    if city == "New York":
        value = int(90,000,000)
    elif city == "San Francisco": 
        value = int(80,000,000)
    elif city == "Houston":
        value = int(70,000,000,000)
    elif city == "Los Angeles":
        value = int(60,000,000)
    elif city == "Las Vegas":
        value = int(50,000,000)
    elif city == "Detroit":
        value = int(40,000,000)
    elif city == "New Orleans":
        value = int(30,000,000)
    elif city == "San Jose":
        value = int(20,000,000)
    elif city == "Philadelphia":
        value = int(10,000,000)
    else:
        strength = random.randint(int(10,000,000), int(100,000,000))
    return value

def taxValue():
    tax = int(raw_input("What tax value do you desire (10,000,000-100,000,000): "))
    if tax > 100,000,000 or tax < 10,000,000:
        tax = random.randint(10,000,000, 100,000,000)
    taxValue = float(tax) * 5
    return taxValue

def citizens(value, taxValue):
    population = random.random()
    happiness1 = (value + taxValue ** 3) / population
    happiness2 = (value + taxValue ** 3) / population
    if happiness1 > happiness2
        return True
    else: 
        return False

def output(playerCity, enemyCity, taxValue):
    return


def main():
    playerCity = raw_input("Which city do you choose?: ")
    enemyCity = raw_input("Which city does enemy 1 choose?: ")

    

    
