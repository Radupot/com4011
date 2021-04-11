def sum_weights(w,w1):
  total_w=w+w1
  return total_w

def calc_avg_weight(w,w1):
  sum_weights(w,w1)
  return sum_weights(w,w1)/2

def run():
  print("What is the weight of Beep?")
  w=int(input())
  print("What is the weight of Bop?")
  w1=int (input())
  sum_weights(w,w1)

  print("What would you like to calculate?(sum or average")
  user_response=input()
  if user_response=="sum":
    print("The sum of Beep and Bop's weight is",sum_weights(w,w1))
  elif user_response=="average":
    print("The average of Beep and Bop's weight is",calc_avg_weight(w,w1))
  else:
    print("You have to enter sum or average!!")


run()