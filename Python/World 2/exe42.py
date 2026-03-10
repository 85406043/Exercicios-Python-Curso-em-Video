#variables
firstAngle = float(input("Enter a first Angle: "))
secondAngle = float(input("Enter a second Angle: "))
thirdAngle = float(input("Enter a third Angle: "))

#conditions
if firstAngle == secondAngle == thirdAngle :
  print("Perfect Triangle! Triangle Equilateral.")
elif firstAngle == secondAngle or secondAngle == thirdAngle or firstAngle == thirdAngle:
  print("Triangle Isosceles.")
else:
  print("Triangle Scalene.")
