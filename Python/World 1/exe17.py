#import module
import math
#formule= h² = co² + ca² h = √(co² + ca²)
#3 angles]
opposite_leg = float(input("Opposite Leg: "))
adjcent_leg = float(input("Adjcent Leg: "))
#calculate
hypotenuse = (opposite_leg ** 2) + (adjcent_leg ** 2)
root_hypotenuse = math.sqrt(hypotenuse)
#show result
print("The Hypotenuse will measure {:.2f}.".format(float(root_hypotenuse)))
