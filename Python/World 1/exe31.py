#km
km = float(input("Enter a KM: "))
#conditions
if km <= 200:
  calc = km * 0.50
  print(f"Adding the rate of R$0,50 for each kilometer, your trip will result in an expensive of R${calc}.")
else:
  calc = km * 0.45
  print(f"Adding the rate of R$0,45 for each kilometer, your trip will result in an expensive of R${calc}.")
