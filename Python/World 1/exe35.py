#angles
firstAngle = float(input("Enter a Angle: "))
secondAngle = float(input("Enter a Angle: "))
thirdAngle = float(input("Enter a Angle: "))
#conditions
if firstAngle < secondAngle + thirdAngle and secondAngle < firstAngle + thirdAngle and thirdAngle < firstAngle + secondAngle:
  print("These angles create a perfect triangle.")
else:
  print("These angles do not create a triangle.")
