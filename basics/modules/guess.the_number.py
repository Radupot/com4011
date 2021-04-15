import random 

print("Please enter the minimum value:")
min_value=int(input())
print("Please enter the maximum value:")
max_value=int(input())

random_n= random.randrange(min_value,max_value,1)

print("I am thinking of a number between {} and {}. Can  you guess what it is?".format(min_value,max_value))

guess = 0

while (guess != random_n):
  guess=int(input())

  if (guess == random_n) :
    print("Congratulations. You guessed my number, lucky!\n")
    break
  elif (guess < random_n):
    print("Your guess is to low\nTry again")
   
  else : 
    print("Your guess is to high.\nTry again")

print("Game over")