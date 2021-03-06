def BAI(hip_circumference_cm, height_m): 
    bai = ((hip_circumference_cm) / (height_m**float(1.5))) - 18
    return bai

def output(name, hip_circumference_cm, height_m, bai, info):
    return """
Hello there, {}!
Did you know your BAI (Body Adiposity Index) is:
({} / {}**float(1.5)) - 18 = {}%
BAI Classifications for Men: If your BAI is less than 8%, you are underweight. If it is 8 to 21%, you are healthy. If it is greater than 21%, you are overweight. If it is geater than 26%, you are obese.\nBAI Classifications for Women: If your BAI is less than 21%, you are underweight. If it is 21% to 33%, you are healthy. If it is greater than 33%, you are overweight. If it is greater than 39%, you are obese.
""".format(name, hip_circumference_cm, height_m, bai, info)

def main():
    name = raw_input("What's your name?: ")
    hip_circumference_cm = raw_input("Type your hip circumference in cm: ")
    height_m = raw_input("Type your height in m: ")
    bai = BAI(float(hip_circumference_cm), float(height_m))
    info = "BAI Classifications for Men: If your BAI is less than 8%, you are underweight. If it is 8 to 21%, you are healthy. If it is greater than 21%, you are overweight. If it is geater than 26%, you are obese.         BAI Classifications for Women: If your BAI is less than 21%, you are underweight. If it is 21% to 33%, you are healthy. If it is greater than 33%, you are overweight. If it is greater than 39%, you are obese."
    print output(name, hip_circumference_cm, height_m, bai, info)

main()
