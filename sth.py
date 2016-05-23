def function4(a, b, c):
    if a > b and a > c:
        return 1 + function4(b+1, c, a)
    elif b > a or b > c:
        return 1 - function4(b-1, c, a)
    else:
        return a + b+ c
        

def main():
    print function4(1, 2, 3)
    print function4(3, 2, 1)
    print function4(1, 3, 2)
main()
