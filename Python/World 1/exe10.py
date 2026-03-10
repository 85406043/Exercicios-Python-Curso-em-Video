#I need an initial value
real = float(input("How much money do you have? R$ "))
#I need to convert the currency from reais to dollars.
sum = real / 5.20
#Show result
print("With R${:.2f} you can buy ${:.2f}".format(real, sum))
