import random
import math

def output(number1, number2,):
    return """
I'm thinking of a number from {} to {}.
""". format(number1, number2)

def result(target, guess, offby):
    if target > guess:
        print """
The target was {}.
Your guess was {}.
That's under by {}.
""". format(target, guess, offby)

    elif target == guess:
        print """
The target was {}.
Your guess was {}.
You're a mind reader!
""". format(target, guess, offby)
    
    else:
            print """
The target was {}.
Your guess was {}.
That's over by {}.
""". format(target, guess, offby)
    
def main():
    number1 = int(raw_input("What is the minimum number? "))
    number2 = int(raw_input("What is the maximum number? "))
    print output(number1, number2)
    guess = int(raw_input("What do you think it is? "))
    target = random.randint(int(number1), int(number2)) 
    offby = abs(int(target) - int(guess))
    result(target, guess, offby)
main()
