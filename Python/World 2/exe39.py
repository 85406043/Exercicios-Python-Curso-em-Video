import datetime
year  = int(input("Enter a Year: "))
#age
actuallyYear = datetime.date.today().year
ageActually = actuallyYear - year
print(ageActually)

#conditions
#minor
if ageActually < 18:
  print("Minor;")
  calcAge = 18 - ageActually
  yearEnlistment = year + 18
  print(f"{calcAge} years until enlistment.")
  print(f"Years of enlistment is {yearEnlistment}.")

#quite
elif ageActually == 18:
  print("Enlist urgently.")

#adult
elif ageActually > 18:
  print("Adult;")
  lateTime = ageActually - 18
  yearEnlistment = actuallyYear - lateTime
  print(f"{lateTime} years have passed since your enlistment.")
  print(f"The year of enlistment was {yearEnlistment}.")
