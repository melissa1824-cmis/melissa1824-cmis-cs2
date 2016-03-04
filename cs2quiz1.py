#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# The symbol "=" is an assignment operator, and it is used to assign a value to a variable.
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that performs a computation. 
#
#3 1pt) What does the keyword "return" do?
# The keyword "return" executes the function. The result of a function is the return value.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean - True, False
#	2: integer - 3, 5
#	3: floating point - 1.5, 6.7
#	4: string - "Hello" "Goodbye"
#	5: tuple - tuple("Hello")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition specifies the name of a new function and the sequence of statements that execute when the functions is called. A function call is a statement that executes a function. It consists of the function name folld by an argument list. 
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Debugging
#	2: Testing
#	3: Implementation
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this
#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
import math

def area1(c1):
	c1 = raw_input("C1")
	return (c1)

def area2(diameter2):
	c2 = raw_input("C2")
	return (c2)

def area3(diameter3):
	c3 = raw_input("C3")
	return (c3)

def circle_area1(area1):
	return (a * 2)** 2 * math.pi

def circle_area2(area2):
	return (b * 2)** 2 * math.pi

def circle_area3(area3):
	return (c * 2)** 2 * math.pi

def diameter(c1): 
    diameter = math.pi * (2 * (math.sqrt(area1 / math.pi))) 

def diameter(c2): 
    diameter = math.pi * (2 * (math.sqrt(area2 / math.pi))) 

def diameter(c3): 
    diameter = math.pi * (2 * (math.sqrt(area3 / math.pi))) 



def output(c1, c2, c3):
    return """
C1: math.pi * (2 * (math.sqrt((area1 / math.pi))) 
C2: math.pi * (2 * (math.sqrt((area2 / math.pi))) 
C3: math.pi * (2 * (math.sqrt((area3 / math.pi)))
""".format(c1, c2, c3)

def main():
    C1 = raw_input("Area of C1:") 
    C2 = raw_input("Area of C2:")   
    C3 = raw_input("Area of C3:")   

    print output(c1, c2, c3)

main()

