#variables numbers
firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter a Second number: "))
thirdNumber = int(input(" Enter a Third number: "))

#variables Larger and Smaller
largerNumber = smallerNumber = firstNumber

#conditions
if secondNumber > firstNumber:
  largerNumber = secondNumber
if secondNumber < firstNumber:
  smallerNumber = secondNumber

if thirdNumber > firstNumber:
  largerNumber = thirdNumber
if thirdNumber < firstNumber:
  smallerNumber = thirdNumber

print(f"Larger Number: {largerNumber}")
print(f"Smaller Number: {smallerNumber}")
