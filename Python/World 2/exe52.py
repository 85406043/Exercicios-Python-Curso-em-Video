#modules
from colorama import Fore, Style

#variable
firstNumber = int(input("Enter a number: "))
listNumber = []
counter = 0

#loop repeat
for root in range(1, 11):
  if firstNumber % root == 0:
    listNumber.append(f"{Fore.YELLOW}{root}{Style.RESET_ALL}")
    counter += 1
  else:
    listNumber.append(f"{Fore.RED}{root}{Style.RESET_ALL}")

#loop repeat
for item in listNumber:
  print(item, end=" ")

#conditions
if counter == 2:
  print("\nPrime number")
else:
  print(f"\nIt was divided {counter} times.")
  print("It's not a Prime number")
