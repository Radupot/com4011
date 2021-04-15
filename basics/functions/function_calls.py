#program that can decipher cryptic clues

#displaying the box
def display_box(user_response):
  print(" ________")
  print("|        |")
  print("|   {} |".format(user_response))
  print("|________|")

#lower case func
def lower_case(user_response):
  return(str.lower(user_response))

#upper case func
def upper_case(user_response):
  return(str.upper(user_response))

#mirrorer word
def mirrored(user_response):
  for position in range(len(user_response)-1,-1,-1):
    print(user_response[position],end="")

#repeat function
def repeat(user_response):
  print("How many times shall I repeat the word?")
  action=int(input())
  for i in  range(action):
    if (i %2 == 0):
      print(lower_case(user_response))
    else:
      print(upper_case(user_response))


def run():

  #asking user for a word
  print("Enter a word.")
  user_response=input()

  action=0 

  while (action != 6):
    #printing the menu
    print("1) Display in a Box\n2) Display Lower-case\n3) Display Upper-case\n4) Display Mirrored\n5) Repeat\n6) Exit")
    #asking user for a choice from the menu
    action=int(input()) 
     #linking the menu with the functions
    if action == 1:
      display_box(user_response)
    elif action == 2:
      print(lower_case(user_response))
    elif action == 3:
      print(upper_case(user_response))
    elif action == 4:
     mirrored(user_response)
    elif action == 5:
     repeat(user_response)
    elif (action == 6):
        break
    else :
      print("Unknown number!!")


run()
