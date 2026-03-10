# I need a initial number: Days and KM
days = float(input("How many days it rented: "))
km = float(input("How many KM traveled: "))
# Formula: Total Price = (Days × 60) + (Km × 0,15)
sum = (days * 60) + (km * 0.15)
# Show result
print("Based on the number of days rented and kilometers traveled, the amount to be paid will be R${:.2f}.".format(sum))
