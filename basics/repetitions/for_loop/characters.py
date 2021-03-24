print("What strange markings do you see?")
markings=str(input())


print("\nIdentifying...\n")

for position in range(0,len(markings),1):
  print("Index {}:".format(position), markings[position])

print("\nDone!")