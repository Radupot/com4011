def observed():
  observations=[]
  for x in range(5):
    print("Please enter an observation:")
    observations.append(input())
  return observations

def remove_observations(observations):
 loop= True
 while(loop):
  print("Do you wish to remove an observation?(yes/no")
  answer=input()
  if (answer == "yes"):
    print("What observation do you wish to remove?")
    answr=input()
    observations.remove(answr)
    print("Done!")
  else:
    loop = False
    
def run():
  observations=observed()
  remove_observations(observations)

  observations_set = set()
  for observation in observations:
   data = (observation, observations.count(observation))
   observations_set.add(data)

  for data in sorted(observations_set):
    print(f"{data[0]} observed {data[1]} times.")
  
run()




