def directions():
  directions=["MoveForward","Move Backward","Turn Left","Turn Right"]
  return directions

def menu():
  print("Please select a direction")
  direction=directions()
  for index in range(len(direction)):
    print(f"{index}:{direction[index]}")
  index=int(input())
  return direction[index]

def run():
  route=[]
  print("Working on escape route...\n")
  for i in range(5):
    route.append(menu())
  print(f"Escape route:{route}")

run()