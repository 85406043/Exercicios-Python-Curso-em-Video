"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""


firstAngle = float(input("Enter a first Angle: "))
secondAngle = float(input("Enter a second Angle: "))
thirdAngle = float(input("Enter a third Angle: "))

if firstAngle == secondAngle == thirdAngle :
  print("Perfect Triangle! Triangle Equilateral.")
elif firstAngle == secondAngle or secondAngle == thirdAngle or firstAngle == thirdAngle:
  print("Triangle Isosceles.")
else:
  print("Triangle Scalene.")
