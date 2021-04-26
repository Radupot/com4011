import os


def cwd():
  path = os.getcwd()
  print(f"Current Working directoy is: {path}")
  print("The directory cointains the following:")

  for file in os.listdir(path):
   print(file)

  
def run():
  print("Processing...")
  cwd()

run()