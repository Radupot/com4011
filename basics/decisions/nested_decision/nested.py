#Ask user what type of cover the book has

print("What type of cover does the book have?")
cover = input()

if (cover == "soft"):
  print("Is the book perfect-bound?")
  book = input()
  if ( book == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else :
    print("Soft covers with coils or stiches are great for short books!")

else : 
  print("Books with hard covers can be more expensive!")