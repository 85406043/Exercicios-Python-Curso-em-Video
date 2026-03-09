#loop
while True:
  #variable
  sexUser = str(input("Your Sex: ")).upper().replace(" ", "")
  #conditions
  if sexUser != "F" and sexUser != "M":
    print("Error: Type M or F.")
    pass
  else:
    print(f"Sucess! Your gender has been successfully registered.")
    break

