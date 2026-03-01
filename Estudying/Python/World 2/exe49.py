print("Multiplication Table")
#variable
numberTable = int(input("Enter a number: "))
#loop repeat
print("-"*20)
for multTable in range(1, 11):
  calcNumber = numberTable * multTable
  print(f"{numberTable} x {multTable:>2} = {calcNumber}")
print("-"*20)
