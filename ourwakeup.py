import math

def intro():
	return "This  program will ask you for 5 integer or float values. It will calculate the average of all valus from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd."

def average():
	average = float((n0 + n1 + n2 + n3 + n4) / 5)
	return

def integer():
	integer = int(average)
	return

def evenorodd(average):
	intaverage = int(average)/2
	if intaverage == int:
		evenorodd = "The integer part is even."
		return evenorodd
	else:
		evenorodd = "The integer part is odd."
		return evenorodd

def output(intro, average, integer, evenorodd):
	print """
The average is {}.
The integer part of the average is {}.
The integer part is {}.
""".format(average, integer, evenorodd)

def main():
	print intro
	n0 = float(raw_input("n0: "))
	n1 = float(raw_input("n1: "))
	n2 = float(raw_input("n2: "))
	n3 = float(raw_input("n3: "))
	n4 = float(raw_input("n4: "))
	average = float((n0 + n1 + n2 + n3 + n4) / 5)
	intaverage = int(average)/2
	evenorodd(average)
	print(intro, average, integer, evenorodd)
	
main()
