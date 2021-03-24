print("How many numbers should I sum up?")
#user input
numbers = int(input())
i=1
t= 0

while (i <= numbers):
  print("Please enter the number {} of {}".format(i,numbers))
  number= int(input())
  t=t+number
  i=i+1
  

print("The answer is",t)