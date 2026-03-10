#module
import datetime

#list ages
listMinor = []
listOfLegalAGe = []

#loop
for age in range(1, 8):
  #age block
  ageUser = int(input("Your year of birth: "))
  yearActually = datetime.date.today().year
  ageUserActually = yearActually - ageUser
  #conditions
  if ageUserActually < 18:
    listMinor.append(ageUserActually)
  else:
    listOfLegalAGe.append(ageUserActually)

#show result
print(f"""
{len(listMinor)} people are minors.
{len(listOfLegalAGe)} people are already adults.
""")
