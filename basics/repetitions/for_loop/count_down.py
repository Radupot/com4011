#printing the message
print("How far are we from the cave?")

#user input
distance = int(input())
steps = 0

#displaying the remaining steps using a for loop

for count in range(distance,0,-1):
   print("{} steps remaining".format(distance))
   distance -= 1 
   
print("")
print("We have reachede the cave!")