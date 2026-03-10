#initial banner
number = int(input("Enter a Int number: "))
print("-="*50)
print("""
Options:
      1 - Binary
      2 - Octal
      3 - Hexadecimal
""")
print("-="*50)
option = int(input("Enter a option: "))
print("-="*50)

#variables and conditons
if option == 1 :
  binary = bin(number)
  print(f"{number} converted to binary equals {binary}.")
elif option == 2 :
  octal = oct(number)
  print(f"{number} converted to Octal equals {octal}.")
elif option == 3 :
  hexadecimal = hex(number)
  print(f"{number} converted to Hexadecimal equals {hexadecimal}.")
elif option != 1 and 2 and 3:
  print("Enter a valid option!")
