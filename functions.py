import math
def add(a, b):
    return a + b
a = add(3, 4)

def sub(a, b):
    return a - b
b = sub(5, 3)

def mul(a, b):
    return a * b
c = mul(4, 4)

def div(a, b):
    return a / b
d = div(2, 3)

def hours_from_seconds(a):
    return a / 3600
hours_from_seconds(86400)

def circle_area(a):
    return a**2 * math.pi
circle_area(5)

def sphere_volume(a):
	b = float(4/3)
	return float(4/3) * math.pi * a**3
sphere_volume(5)

def avg_volume(a, b):
    c = float(a/2)
    d = float(b/2)
    e = float(4/3)
    return ((e)*math.pi*(c**3)) + ((e)*math.pi*(d**3))/2
avg_volume(10, 20)

def area(a, b, c):
    s = (a + b + c)/2
    return math.sqrt(float((s(s-a)(s-b)(s-c))))
area(1, 2, 2.5)

def right_align(a):
	print str(" "*40 - len(a)) 

def center(a):
    print str(" "*80 - len(a))

def msg_box(txt):
	return "+" + ((len(txt)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (txt) + (2*" ") + "|" + "\n" + "+" + ((len(txt)+4)*"-") + "+"
msg_box("Hello")

a = add(3, 4)
print a
b = sub(5, 3)
print b
c = mul(4, 4) 
print c
d = div(2, 3)
print d
e = hours_from_seconds(86400)
print e
f = circle_area(5)
print f
g = sphere_volume(5)
print g
h = avg_volume(10, 20)
print h

