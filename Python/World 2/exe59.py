#module
from time import sleep as sp
#variables and lists
listNumbers = []
condition = False
numberOne = int(input("Digite um número: "));listNumbers.append(numberOne)
numberTwo = int(input("Digite outro número: "));listNumbers.append(numberTwo)

#loop
while condition == False:
  menu = int(input("""=-=-=-=-=-=-=-=-=-=-=-=-=-=-
      [ 1 ] Somar
      [ 2 ] Multiplicar
      [ 3 ] Maior
      [ 4 ] Novos números
      [ 5 ] Sair
  => Sua escolha: """))

  #conditions
  if menu <= 5:
    if menu == 1:
      soma = numberOne + numberTwo
      print("=-"*14)
      print(f"{numberOne} + {numberTwo} = {soma}.")
    elif menu == 2:
      multi = numberOne * numberTwo
      print("=-"*14)
      print(f"{numberOne} x {numberTwo} = {multi}")
    elif menu == 3:
      print("=-"*14)
      print(f"Maior número: {max(listNumbers)}")
    elif menu == 4:
      print("=-"*14)
      listNumbers.clear()
      numberOne = int(input("Digite um número: "));listNumbers.append(numberOne)
      numberTwo = int(input("Digite outro número: "));listNumbers.append(numberTwo)
    elif menu == 5:
      print("=-"*14)
      condition = True
      print("Até a próxima...")
  else:
    print("=-"*14)
    print("Opção inválida...")
