import random


# Define a function that asks the user for input and DOESN'T QUIT until the user returns something valid
# In this case, "valid" means an integer between 1 and 100 (inclusive)


def get_input():
  while True:
    try:
     user = int(input("Please select an integer between 1 and 100(inclusive): "))
     if user > 100 or user < 1:
      print("Please select an integer between 1 and 100(inclusive):")
     else:
        break
    except ValueError:
      print("your input is not an integer")
   
  return user


# Define a function that compares the user's input to the answer
# Returns a string that indicates the answer is higher or lower than the input


def compare_input(user, answer):
  if user > answer:
    print("the answer is lower than your input")
    return False
  elif user < answer:
    print("the answer is higher than your input")
    return False
  elif user == answer:
    print("The answer is equal to your input. congratulations! You find the answer.")
    return True



# Define your main() function


def main():
  # Set a random number between 1 & 100
  answer = random.randint(0,100)
  print(answer)
  while True:
    valid_user = get_input()
    if compare_input(valid_user , answer) == True:
      break




 
if __name__== "__main__":
  main()

