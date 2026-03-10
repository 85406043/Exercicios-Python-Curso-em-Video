#variables
numberFirstInt = int(input('Enter a number: '))
numberSecondInt = int(input('Enter a second number: '))

#conditions
if numberFirstInt > numberSecondInt:
  print(f"The {numberFirstInt} is greater than the {numberSecondInt}.")
elif numberSecondInt > numberFirstInt:
  print(f"The {numberSecondInt} is greater than the {numberFirstInt}.")
elif numberFirstInt == numberSecondInt:
  print("The numbers are equals.")
