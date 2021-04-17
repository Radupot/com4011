def functions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction")
  local = functions()
  for index in range(len(local)):
    print(f"{index}:{local[index]}")

def run():
  menu()


run()