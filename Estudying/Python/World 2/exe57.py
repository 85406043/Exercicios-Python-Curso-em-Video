#variable
condition = False
#loop
while condition == False:
  sexUser = str(input("Your Sex: ")).upper().replace(" ", "")
  #conditions
  if sexUser != "F" and sexUser != "M":
    print("Error: Type F or M.")
  else:
    condition = True
    print("Success! Your gender has been successfully registered.")
