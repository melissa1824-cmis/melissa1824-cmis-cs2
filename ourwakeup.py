import math

def intro():
	print "This  program will ask you for 5 integer or float values. It will calculate the average of all valus from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd."

def average():
	average = float((n0 + n1 + n2 + n3 + n4) / 5)
	return

def therange(n0, n1, n2, n3, n4):
	if n0 < 0 or n0 > 9:
		print "n0 out of range."
		exit()
	elif n1 < 0 or n1 > 9:
		print "n1 out of range."
		exit()
	elif n2 < 0 or n2 > 9:
		print "n2 out of range."
		exit()
	elif n3 < 0 or n3 > 9:
		print "n3 out of range."
		exit()
	elif n4 < 0 or n4 > 9:
		print "n4 out of range."
		exit()

def integer():
	integer = int(average)
	return

def findevenorodd(intaverage):
	if (intaverage/2) == int:
		evenorodd = "The integer part is even."
	else:
		evenorodd = "The integer part is odd."
		return evenorodd

def output(average, intaverage, evenorodd):
	return """
The average is {}.
The integer part of the average is {}.
The integer part is {}.
""".format(average, intaverage, evenorodd)

def main():
	intro()
	n0 = float(raw_input("n0: "))
	n1 = float(raw_input("n1: "))
	n2 = float(raw_input("n2: "))
	n3 = float(raw_input("n3: "))
	n4 = float(raw_input("n4: "))
	average = float((n0 + n1 + n2 + n3 + n4) / 5)
	therange(n0, n1, n2, n3, n4)
	intaverage = int(average)
	evenorodd = findevenorodd(intaverage)
	print output(average, intaverage, evenorodd)
	
main()
