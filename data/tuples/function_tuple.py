def likelihood():
  likelihoods = (50,32,27,99,4)
  return max(likelihoods),min(likelihoods)

def run():
  min_max=likelihood()
  print(f"Minimum likelihood of falling: {min_max[1]}")
  print(f"Maximum likelihood of falling: {min_max[0]}")

run()