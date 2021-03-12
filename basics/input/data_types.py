#Program that calculates BMI(body mass index)

print("What is your name, human?")
name = str(input())

print("How old are you?")
age = int(input())

print("How tall are you(in meters)?")
tall = float(input())

print("How much do you weight(in kg?")
weight = int(input())


print("{} you are {} years old and your bmi is {:.2f}".format(name,age,weight/tall**2))