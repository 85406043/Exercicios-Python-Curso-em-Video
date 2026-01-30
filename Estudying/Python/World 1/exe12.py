# number initial
price = float(input("What is this value? R$"))
# calculate (rule of three)
rule_of_three = (price * 5) / 100
discount = price - rule_of_three
# show
print("The value, with a 5% discount is R${:.2f}".format(discount))
