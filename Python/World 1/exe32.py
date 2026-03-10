#i need year
year = int(input("Enter a Year: "))
#conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("It's a leap Year.")
else:
  print("This year is not a leap Year.")
