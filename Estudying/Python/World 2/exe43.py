"""BMI below 18.5: Underweight

- Between 18.5 and 25: Ideal Weight

- 25 to 30: Overweight

- 30 to 40: Obesity

- Above 40: Morbid Obesity"""

#variables
kiloGram = float(input("Enter your Weight: "))
heightUser = float(input("Enter your Height: "))

#Calc variables
calcHeight = heightUser**2
calcImc = kiloGram / calcHeight

#conditions
if calcImc < 18.5:
  print(f"Your IMC is {calcImc:.1f}.")
  print("Underweight.")

elif calcImc < 25:
  print(f"Your IMC is {calcImc:.1f}.")
  print("Ideal Weight")

elif calcImc < 30:
  print(f"Your IMC is {calcImc:.1f}.")
  print("Overweight.")

elif calcImc < 40:
  print(f"Your IMC is {calcImc:.1f}.")
  print("Obesity.")

elif calcImc > 40:
  print(f"Your IMC is {calcImc:.1f}.")
  print("Morbid Obesity.")
