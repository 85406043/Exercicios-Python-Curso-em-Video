#variables
print("=-" * 50)
print("Credit Analysis")
print("=-" * 50)
valueLoan = float(input("Value of your Loan: R$ "))
salaryUser = float(input("Your Salary: R$ "))
years = float(input("How many years: "))

#formule Approved = (valueHome ÷ (Years × 12)) ≤ (Salary × 0,30)
totalMonths = years * 12
provisionLoan = valueLoan / totalMonths
limitLoan = salaryUser * 0.30
remainderOfSalary = salaryUser - provisionLoan

#show result
if provisionLoan <= limitLoan:
  print("=-" * 50)
  print("Loan approved!")
  print("=-" * 50)
  print(f"Loan Installments: R${provisionLoan:.2f}")
  print(f"Remainder of Salary: R${remainderOfSalary:.2f}")
  print("=-" * 50)
else:
  print("=-" * 50)
  print("Loan denied!")
  print("=-" * 50)
  print("The installments amounts execeeded 30% of your salary.")
  print(f"Loan Installments: R${provisionLoan:.2f}")
  print("=-" * 50)
