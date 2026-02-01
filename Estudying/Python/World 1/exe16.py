#import module
import math
#number initial
number_trunc = float(input("Enter a number: "))
#call the module
trunc = math.trunc(number_trunc)
#show result
print("The value entered was {}, and its integer portion is {}.".format(number_trunc, trunc))
