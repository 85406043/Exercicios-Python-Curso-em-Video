#list
listWeight = []
#loop
for weight in range(1, 6):
  weightUser = float(input("Enter your weight: "))
  listWeight.append(weightUser)
#show result
print(f"Highest weight recorded: {max(listWeight)}kg")
print(f"Lowest weight recorded: {min(listWeight)}kg")
