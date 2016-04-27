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

def adder():
    n = raw_input("n: ")
    while True:
        input = raw_input("n: ")
        if input == "":
            break

def main():
    adder()

main()
