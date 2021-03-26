def interests():
  print("Enter yourt interests, one after the other, and enter \"stop\" when finished" )
  set1 = set()
  activity = ""
  while(activity != "stop"):
    activity=input()
    set1.add(activity)
  return set1

def tinderThesecond():
  print("First person:")
  P1set = interests()
  print("Second person:")
  P2set = interests()
  common = P1set.intersection(P2set)
  if len(common) > 4:
    print(f"Yay - you are a match! You have {len(common)} interests in common")
  else:
    print(f"Well, I don't think it will work out :( You only have {common.size()} interests in common".format)

tinderThesecond()