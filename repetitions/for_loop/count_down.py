#printing the message
print("How far are we from the cave?")

#user input
distance = int(input())

#displaying the remaining steps using a for loop

for count in range(distance,0,-1):
   print(count, "steps remaining")
   
print("")
print("We have reachede the cave!")