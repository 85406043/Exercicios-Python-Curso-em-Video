#import module
import math
#i need a angle
angles = float(input("Pleace it at any angle: "))
#formule Radianos = Graus × (π / 180) Graus = Radianos × (180 / π)

#caculate of angles sen cos and tan
sin = math.sin(math.radians(angles))
cos = math.cos(math.radians(angles))
tan = math.tan(math.radians(angles))
#show result
print("Sine: {:.2f}\nCosine: {:.2f}\nTangent: {:.2f}".format(sin, cos, tan))
