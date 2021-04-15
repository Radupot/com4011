print("What phrase do you see?")
phrase= input()

print("\nReversing...\n")

phrase_reversed= ""

for i in phrase :
  phrase_reversed= i+phrase_reversed

print(phrase_reversed)