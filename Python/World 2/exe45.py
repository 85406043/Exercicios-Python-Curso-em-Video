#import modules
import random
import time
#choise user
print("Game Jokenpô")
print("==-"*50)
userChoise = int(input("""Choose between:
      [1] Rock
      [2] Paper
      [3] Scissors
      => """))

#CPU
listCpu = ["Rock", "Paper", "Scissors"]
choiseCPU = random.choice(listCpu)

time.sleep(0.5)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")

#conditions
if userChoise == choiseCPU:
  print("Draw")

elif userChoise != choiseCPU:
  if userChoise == 1 and choiseCPU == "Paper":
    print("User selected Rock")
    print(f"CPU selected {choiseCPU}")
    print("CPU Win")
  elif userChoise == 2 and choiseCPU == "Scissors":
    print("User selected Paper")
    print(f"CPU selected {choiseCPU}")
    print("CPU Win")
  elif userChoise == 3 and choiseCPU == "Rock":
    print("User selected Scissors")
    print(f"CPU selected {choiseCPU}")
    print("CPU win")
  elif choiseCPU == "Rock" and userChoise == 2:
    print("User selected Paper")
    print(f"CPU selected {choiseCPU}")
    print("User Win")
  elif choiseCPU == "Paper" and userChoise == 3:
    print("User selected Scissors")
    print(f"CPU selected {choiseCPU}")
    print("User Wind")
  elif choiseCPU == "Scissors" and userChoise == 1:
    print("User selected Rock")
    print(f"CPU selected {choiseCPU}")
    print("User Win")
