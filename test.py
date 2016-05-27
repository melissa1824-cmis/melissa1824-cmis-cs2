#while 3 > 2:
    #print ":)"

#x = 0
#while x < 10:
    #print x
    #x += 1

#x = 10
#while x >= 0:
    #print x
    #x -= 1

#def countdown(x):
    #while x >= 0:
        #print x
        #x -= 1

#def countup(x):
    #while x <= 10:
        #print x
        #x += 1

#def count(x):
    #while x > 0:
        #print x
        #x -= 1
    #while x < 0:
        #print x
        #x += 1

#def countFrom2(x, y):
    #while x < y:
        #print x
        #x += 1
    #while x >= y:
        #print x
        #x -= 1

#def addodds(n):
    #sum = 0
    #if n > 0:
        #while n > 0:
            #if n % 2 == 1:
                #sum += n
            #n -= 1
    #elif n < 0:
        #while n < 0:
            #if n % 2 == 1:
                #sum += n
            #n += 1
    #print sum

#def grid(w, h):
    #if w > h:
        #while w > h:
            #print "."
            #w -= 1
    #elif w < h:
        #while w < h:
            #print "."
            #w += 1

def grid(w, h):
    out = ""
    out2 = ""
    x = 0
    while x < w:
        out += "."
        x += 1
    y = 0
    while w > h:
        out2 += "."
        w -= 1
    return out
    return out2
print grid(10,10)
            


#countdown(7)
#countup(-6)

#count(-100)
#count(100)

#countFrom2(-100, 0)
#countFrom2(1, 100)

#addodds(-10)

#grid(0,10)

