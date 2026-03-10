#i need km
velocityCar = float(input("Enter the car's speed: "))
#conditions
if velocityCar == 80:
  #show result
  print("You are average.")
  print(f"Average {velocityCar}KM.")
else:
  #calculate
  kmExceeded = velocityCar - 80
  calcFine = kmExceeded * 7
  #show result
  print(f"You exceeded the average by {kmExceeded}KM above (80KM standard).")
  print(f"Thefore, your fine will be R${calcFine}.")
