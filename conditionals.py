import random

#My game will be like Monopoly. You choose a city from the list for yourself and your opponent. Each city has a different value (random value generated = how much the city is worth in dollars). After choosing a city, a tax value is subtracted from the value of the city. This tax value is randomly generated. If the final value you have is higher than the opponent's, you win. If not, you lose. *** Happiness of citizens is important. *** 

def value(city):
    if city == "Washington":
        value = 100,000,000
    if city == "New York":
        value = 90,000,000
    elif city == "San Francisco": 
        value = 80,000,000
    elif city == "Houston":
        value = 70,000,000,000
    elif city == "Los Angeles":
        value = 60,000,000
    elif city == "Las Vegas":
        value = 50,000,000
    elif city == "Detroit":
        value = 40,000,000
    elif city == "New Orleans":
        value = 30,000,000
    elif city == "San Jose":
        value = 20,000,000
    elif city == "Philadelphia":
        value = 10,000,000
    else:
        value = random.randint((10,000,000), (100,000,000))
    return value

def taxValue():
    tax = int(raw_input("What tax value do you desire (10,000,000-100,000,000): "))
    if tax > int(100,000,000) or tax < int(10,000,000):
        tax = random.randint(10,000,000, 100,000,000)
    taxValue = float(tax) * 5
    return taxValue

def citizens(playerValue, enemyValue, taxValue):
    population = random.random()
    happiness1 = (value + taxValue ** 3) / population
    happiness2 = (enemyValue + taxValue ** 3) / population
    return 

def total(playerValue, taxValue, citizens):
    player1result = playerValue + tax + happiness1
    player2result = value + tax + happiness2
    return
    if player1result > player2result:
        return True
    else:
        return False

def result(playerValue, taxValue1, result1):
    if result == True:
        msg = "You won! Your city is worth more!"
    else:
        msg = "You lost :( Your opponent's city is worth more."
    return """
Your city's total value: {}
Your opponent's city's total value: {}
""".format(playerValue, taxValue1, result1)

def main():
    playerCity = raw_input("Which city do you choose?: ")
    enemyCity = raw_input("Which city does enemy 1 choose?: ")

    playerValue = value(playerCity)
    enemyValue = value(enemyCity)

    player1tax = taxValue()
    result1 = total(playerValue, player1tax, citizens)

    player2tax = taxValue()
    result2 = total(playerValue, player2tax, citizens)

    output = """
Your city is {}.
Your opponent's city is {}.
""".format(playerCity, enemyCity)
    output += result(playerValue, taxValue, total1)
    output += result(playerValue, taxValue, total2)

    print output
main()
