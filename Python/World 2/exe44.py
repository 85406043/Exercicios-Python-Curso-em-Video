"""– Cash/Check: 10% discount

– Card: 5% discount

– Up to 2 installments by card: formal price

– 3 or more installments by card: 20% interest"""

#variables
priceProduc = float(input("Product Price: "))
payOptions = int(input("""
==-==-==-==-==-==-==-==-==-==-==-==-==
1. Cash/Check
2. Card payment
3. Card in 2 installments
4. Card in 3 or more installments
==-==-==-==-==-==-==-==-==-==-==-==-==
=> """))

#conditions
if payOptions == 1:
  calcPrice = (priceProduc * 10) / 100
  finallyPrice = priceProduc - calcPrice
  print(f"With 10% discount. Debit payment: ${finallyPrice:.2f}.")

elif payOptions == 2:
  calcPrice = (priceProduc * 5) / 100
  finallyPrice = priceProduc - calcPrice
  print(f"With 5% discount. Debit payment: ${finallyPrice}")

elif payOptions == 3:
  calcPrice = priceProduc / 2
  print(f"Divided into 2 installments of ${calcPrice}. No interest.")

elif payOptions == 4:
  intallments = float(input("Divide into how many installments? 3x upwards(20% interest). ==> "))
  if intallments >= 3:
    calcPrice = (priceProduc * 20) / 100
    finallyPrice = priceProduc + calcPrice
    dividedInstall = finallyPrice / intallments
    print(f"{intallments:.0f} installments of the ${dividedInstall}.")
    print(f"Total to pay of ${finallyPrice}.")
  else:
    print("Choose another option in the panel.")
