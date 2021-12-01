print("What is your name human?")
n = input()
print("How old are you (in years)?")
a = int(input()) #Integer representation
print("How tall are you (in meters)?")#
h = float(input()) # Float Representation
print("How much do you weigh (in kilograms)?")
w = float(input())
bmi = w/(h**2)
print(f"{n} you are {a} years old. Your BMI is {bmi}")
