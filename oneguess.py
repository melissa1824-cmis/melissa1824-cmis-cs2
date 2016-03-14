import random

def output(number1, number2):
    return ""
I'm thinking of a number from {} to {}
"".format(number1, number2)

def main():
	number1 = raw_input("What is the minimum number? ")
    number2 = raw_input("What is the maximum number? ")
    print output(number1, number2)

main()
