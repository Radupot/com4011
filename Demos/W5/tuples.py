#initialise an empty set

colours = set()
print(type(colours))

#initialise non-empty set

colors ={"blue","red", "yellow"}
print(type(colors))
print(colors)

#Adding elements to my set
colors.add("purple")
colours.add("red")

print(colours)
print(colors)

#union -joining two sets

set2 = {1,2,3,4}
set1 = colours.union(colors,set2)
print(set1)

