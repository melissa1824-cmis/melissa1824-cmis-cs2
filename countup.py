def countdown(a):
    if a <= 0:
        print "Blastoff!"
    else:
        print a
        countdown(a-1)

def countup(n):
	if n >= 0:
		print "Blastoff!"
	else:
	    print n
	    countup(n+1)

def main():
    countdown(5)
    countup(10)
main()
