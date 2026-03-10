#I need phrase
phrase = input("Write a setence: ").strip().upper()
#I need to process the text
appers = phrase.count("A")
letterA = phrase.find("A")+1
lastPosition = phrase.rfind("A")+1
#show result
print("The letter A appers {} times.".format(appers))
print("The first letter A appeared in the {} position. ".format(letterA))
print("The last letter A appeared in the {} position.".format(lastPosition))
