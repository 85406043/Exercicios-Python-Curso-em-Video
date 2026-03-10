
#i need initial salary
salary = float(input("Enter a Salary: "))
#conditions(calc)
if salary <= 1250:
  calcSalary = (1250 * 15) / 100
  newSalary = calcSalary + salary
  print(f"New salary with an 15% increase: R${newSalary}")

else:
  calcSalary = (1250 * 10) / 100
  newSalary = calcSalary + salary
  print(f"New salary with an 10% increase: R${newSalary}")
