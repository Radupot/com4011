print("Please enter a sequence:(ex:x---x)")
sequence = input()

print("Please enter  the character for the marker")
character = input()

marker_pos1 = -1
marker_pos2 = -1


for count in range(0, len(sequence), 1):
  letter = sequence[count]

  if (letter == character):
      if (marker_pos1 == -1):
          marker_pos1 = count
      else : 
        marker_pos2 = count

print(f"The distance between the markers is {marker_pos2 - marker_pos1 -1}")
