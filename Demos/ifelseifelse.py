print("What is your name?")
n = input()



if len(n)> 9 and dog == "True":
  print("You have a very loooong name!")
  print("Your name contains {} letters".format(len(n)))

elif len(n) > 6:
  print("Your name is a bit long. Consider a nickname")

elif len(n) <3:
  print("Your name is very short")

else :
  print("Your name is quite ok")

print("This is the End of the program!")