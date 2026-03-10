#import module
import random
#variable
condition = False
guessesUser = 0
#loop
while condition == False:
  #i need a number
  numberUser = int(input("Enter a number(INT): "))
  #i need to make the computer think
  computer = random.randint(0, 10)
  #conditions
  if numberUser != computer:
    guessesUser += 1
    print("Try again! Better luck next time...")
    if numberUser < computer:
      print("A little above...")
    elif numberUser > computer:
      print("A little below...")
  #show result
  else:
    guessesUser += 1
    condition = True
    print("Congratulations! You got it right!")
    print(f"It took {guessesUser} guesses to get it right.")
