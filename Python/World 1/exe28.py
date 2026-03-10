#import module
import random
#i need a number
number = int(input("Enter a number(INT): "))
#i need to make the computer think
computer = random.randint(0, 5)
#conditions
if number != computer:
  print("Try again! Better luck next time...")
#show result
else:
  print("Congratulations! You got it right!")
