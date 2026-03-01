import time
#variables
calcOdd = 0
counter = 0
#loop repeat
for odd in range(1, 501, 2):
  if odd % 3 == 0:
    calcOdd += odd
    counter += 1
#result
print(f"Quantity of numbers: {counter}")
print(f"Sum between then: {calcOdd}")
