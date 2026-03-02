#variables
listNumbersPairs = [] #list
sum = 0
#loop
for integer in range(1, 7):
  number = int(input("Enter a number: "))
  if number % 2 == 0:
    listNumbersPairs.append(number)
    sum += number
  else:
    pass
#Show result
print(f"Numbers Pairs: {listNumbersPairs}")
print(f"The sum between pairs: {sum}")
