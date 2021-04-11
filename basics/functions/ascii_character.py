#ascii code for a character

print("Program Started!\nPlease enter a ASCII code")
code = int(input())

if (code >=32 and code <= 126):
  print("The character represented by the ASCII {} is {}".format(code,chr(code)))

else :
  print("Wrong code, mate!")

print("Program Ended!")