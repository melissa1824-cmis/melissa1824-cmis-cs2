def BAI(hip_circumference_cm, height_m): 
    bai = ((hip_circumference_cm) / (height_m**float(1.5))) - 18
    return bai

def output(name, hip_circumference_cm, height_m, bai):
    return """
Hello there, {}!
Did you know your BAI is:
({} / {}**float(1.5)) - 18 = {}%
""".format(name, hip_circumference_cm, height_m, bai)

def main():
    name = raw_input("What's your name?: ")
    hip_circumference_cm = raw_input("Type your hip circumference in cm: ")
    height_m = raw_input("Type your height in m: ")
    bai = BAI(float(hip_circumference_cm), float(height_m))
    print output(name, hip_circumference_cm, height_m, bai)

main()
