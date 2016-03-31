import math
#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 3 == 3
#b) 5 != 8
#c) 45 > 23
#
#2) What does 'return' do?
# returns/prints the value/result of the function.
# 
#3) What are 2 ways indentation is important in python code?
#a) It knows that the next line is part of the function
#b) It knows that the next line of the function has to be executed 
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)
#problem1_b) square root of 3
#problem1_c) 0
#problem1_d) 5
#
#problem2_a) True
#problem2_b) False
#problem2_c) True
#problem2_d) True
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 5
#problem4_b) 5
#problem4_c) 
#problem4_d) 
#

print "Type in 3 different numbers (decimals are OK!)"

def number1(number1):
    number1 = float(raw_input("A: "))
    return number1

def number2(number2):
    number2 = float(raw_input("B: "))
    return number2

def number3(number3):
    number3 = float(raw_input("C: "))
    return number3

def compare(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    else:
        return number3

def output(number1, number2, number3):
    return """
""".format(compare, number1, number2, number3)

def main():
    number1 = float(raw_input("A: "))
    number2 = float(raw_input("B: "))
    number3 = float(raw_input("C: "))
print output(number1, number2, number3)

main()
