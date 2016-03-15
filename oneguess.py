import random
import math

def output(number1, number2,):
    return """
I'm thinking of a number from {} to {}.
""".format(number1, number2)

def result(target, guess, offby):

    if target > guess:
        print """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target, guess, offby)

    elif taget == guess:
        print """
The target {}.
Your guess was {}.
That's equal to {}.
""".format(target, guess, offby)
    
    else target < guess:
        print """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target, guess, offby)
    
def main():
    number1 = raw_input("What is the minimum number? ")
    number2 = raw_input("What is the maximum number? ")
    print output(number1, number2)
    guess = raw_input("What do you think it is? ")
    randomnumber = random(number1, number2)
    offby = abs(target - guess)
main()
