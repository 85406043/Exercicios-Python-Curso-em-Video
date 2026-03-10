import datetime

yearBirth = int(input("Year of birth: "))
yearActuall = datetime.date.today().year
age = yearActuall - yearBirth


if age <= 9 :
  print(f"The athelete is {age} years old.")
  print("Classification: Mirim")

elif age <= 14:
  print(f"The athelete is {age} years old.")
  print("Classification: Infantil")

elif age <= 19:
  print(f"The athelete is {age} years old.")
  print("Classification: Junior")

elif age <= 25:
  print(f"The athelete is {age} years old.")
  print("Classification: Senior")

elif age > 25:
  print(f"The athelete is {age} years old.")
  print("Classification: Master")
