#variables and lists
userOld = ["", 0, ""] #age man
ageWomen = 0 #counter age women
calcAgeUsers = 0 #average

#loop
for data in range(1, 5):
  nameUser = str(input("Your name: ")).replace(" ", "").capitalize()
  ageUser = int(input("Your age: "));calcAgeUsers += ageUser
  sexUser = str(input("Your sex(M/F): ")).replace(" ", "").upper()
  #conditions age man
  if ageUser > userOld[1] and sexUser == "M":
    userOld.clear()
    userOld.append(nameUser)
    userOld.append(ageUser)
    userOld.append(sexUser)
  #women
  elif sexUser == "F" and ageUser < 20:
    ageWomen += 1

#calc average
calcMedia = calcAgeUsers / 4

#show result
print(f"The average age of the group is {calcMedia} anos.")
print(f"The oldest man is {userOld[1]} years old, and his name is {userOld[0]}.")
print(f"In total, there are {ageWomen} women under the of 20.")
