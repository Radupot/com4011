def movements():
  path=["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  local_v = movements()
  print(f"{local_v[0]} for {local_v[1]} steps")
  print(f"{local_v[2]} for {local_v[3]} steps")
  print(f"{local_v[4]} for {local_v[5]} steps")
  print(f"{local_v[6]} for {local_v[7]} steps")

run()