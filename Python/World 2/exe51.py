#variables
firstTerm = int(input("Type a term: "))
reason = int(input("Type a reason: "))
#loop
for n in range(1, 11):
  term = firstTerm + (n - 1) * reason# formule
  print(term,end=" > ")
print("End")
