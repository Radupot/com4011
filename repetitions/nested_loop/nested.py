#ascii emoji

#asking user for inputs

print("How many rows should I have?")
rows= int(input())

print("How many columns should I have?")
columns=int(input())

print("\nHere I go: \n")

#creating the nested for loop 

for number in range(0,rows,1):
  for count in range(0,columns,1):
    print(":)",end="")
  print()