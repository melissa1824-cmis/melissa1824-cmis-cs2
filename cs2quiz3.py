import math
#Section 1: Terminology
# 1) What is a recursive function? 1 point
#   A function that calls itself repeatedly. A function that repeats itself.
#
# 2) What happens if there is no base case defined in a recursive function? 1 point
#   The function doesn't stop repeating itself.         
#
#
# 3) What is the first thing to consider when designing a recursive function? 1 point
#   The conditionals, the base case and recursive case.
#
#
# 4) How do we put data into a function call? 1 point
#   Put data in the arguments/parameters 
#
# 
# 5) How do we get data out of a function call? 
#   Call the function.
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8 point
#a2 = 8 point 
#a3 = -1 point

#b1 = 2 point 
#b2 = 2 point 
#b3 = 4 point 

#c1 = 1 + (-2, 2) 
#c2 = 4 point 
#c3 = 10 + (5, 4) 

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

# 8/10
def average():
    average = float(0)
    print "Average: ", RunningTotal
    calculation(RunningTotal)

def total():
    RunningTotal = float(0)
    print "Running total: ", RunningTotal
    calculation(RunningTotal)

def calculation(RunningTotal):    
    addno = raw_input("Next number: ")
    if addno != "":
        print "Average: ", RunningTotal + float(addno)
        calculation(RunningTotal + float(addno))
	#basecase
    else:
        print "The average of the odds is ", RunningTotal
	#recursive case
 
def main():
    number = int(raw_input("Number: "))
    total()
    
main()

