#ascii code for a character

print("Program Started!\nPlease enter a standard character")
character=input()

if len(character) == 1:
  print("The ASCII code for {} is : {}".format(character,ord(character)))

else:
  print("You have to enter only 1 character")

print("Program Ended!")