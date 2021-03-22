print("How many live cables must I avoid?")
avoid =int(input())

cables = 0

while (cables < avoid):
  cables = cables +1
  print("Avoiding...Done! {} live cables avoided".format(cables))

print("All live cables have been avoided")
