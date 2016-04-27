def countup(n):
	if n >= 10:
		print "Blastoff!"
	else:
	    print n
	    countup(n+1)

def main():
    countup(5)
    return
main()
