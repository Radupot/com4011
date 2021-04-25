def observed():
  observations = []
  for i in range(7):
    print("Please enter an observation")
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  obs=observed()
  words=set()
  for i in range (len(obs)):
    words.add(obs[i])
  set_of_tuples=set()
  
  for item in words:
    count=0
    for i in range(len(obs)):
      if obs[i] == item:
        count +=1
    set_of_tuples.add((item,count))
  print(set_of_tuples)
 

run()