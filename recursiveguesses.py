import math
import random

def round1():
    print "Round 1".format()
    return

def round2():
    print "Round 2".format()
    return

def guess(target, guessn):
    guessn = raw_input("Guess a Number: ")
    if guessn == "":
        print "bye"
    else:
        guess(target, guessn)

def lowhigh(target, guessn):
    if target > guessn:
        print "That's too low".format(target, guessn)
    else:
        print "That's too high".format(target, guessn)


def main():
    round1()
    target = random.randint(0, 100)
    guessn = int(raw_input("Guess a Number: "))
    guess(target, guessn)
    round2()
main()
