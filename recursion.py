def countdown(n):
    if n <= 10:
        print "Blastoff!"
    else:
        print n
        countdown(n-1)

def countup(n):
	if n >= 10:
		print "Blastoff!"
	else:
	    print n
	    countup(n+1)
countup(5)

def countdownTo(start, stop):
    if start < stop:
        print "No!"
    elif start == stop:
        print "Yeah!"
    else:
        print start
        countdownTo(start-1, stop)
countdownTo(10, 5)

def total():
    RunningTotal = float(0)
    print "Running total: ", RunningTotal
    calculation(RunningTotal)

def calculation(RunningTotal):    
    addno = raw_input("Next number: ")
    if addno != "":
        print "Running total: ", RunningTotal + float(addno)
        calculation(RunningTotal + float(addno))
    else:
        print "The sum is ", RunningTotal
 
def number():
    Biggest = float(0)
    print "Number: ", Biggest
    biggest(number)

def biggest(number):
    compareno = raw_input("Number: ")
    if compareno > compareno: 
        print "Biggest number is: " +float(comapreno)
    else:
        compareno < compareno 
        print "Biggest number is: " +
    
def main():
    total()
    number()
    biggest(number)
main()
