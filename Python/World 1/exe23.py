number = int(input("Enter a number: "))
#mathematical formula
unit = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
#show result
print("Unit: {}\nTens: {}\nHundreds: {}\nThousands: {}".format(unit, tens, hundreds, thousands))
