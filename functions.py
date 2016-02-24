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
    return math.sqrt(2.75*(2.75-a)*(2.75-b)*(2.75-c))

def right_align(word):
	return str ((80-len(word))*" " + word) 

print right_align("Hello")

def center(a):
    return str ((40- len(a))*" " + a)

print center("Hello")

def msg_box(txt):
	return "+" + ((len(txt)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (txt) + (2*" ") + "|" + "\n" + "+" + ((len(txt)+4)*"-") + "+"
msg_box("Hello")

print msg_box("Hello")
print msg_box("I eat cats")

a = add(3, 4)
b = sub(5, 3)
c = mul(4, 4) 
d = div(2, 3)
e = hours_from_seconds(86400)
f = circle_area(5)
g = sphere_volume(5)
h = avg_volume(10, 20)
i = area(1.0, 2.0, 2.5)
j = right_align("Hello")
k = center("Hello")

print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(str(j))
print msg_box(str(k))
