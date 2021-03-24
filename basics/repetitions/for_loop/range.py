print("What level of brightness is required?")

bright= int(input())

print("\nAdjusting brightness...")

for count in range(2, bright +1 , 2):
  print("Beep's brightness level:", "*" * count)
  print("Bop's brightness level:", "*" * count)
  print()

print("Adjustments complete!")