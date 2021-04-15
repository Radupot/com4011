#factorial of a number

print("Please enter a number: ")
num=int(input())

factorial = 1
i = 1
while (i<num):
  i=i+1
  factorial= factorial *i

print("The factorial is ",factorial)