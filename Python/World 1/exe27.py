#full name
fullName = input("Enter your full name: ").strip().title()
#first name
firstName = " ".join(fullName.split()[:1])
#last name
lastName = " ".join(fullName.split()[-1:])
#show print
print("Your full name: {}".format(fullName))
print("Your first name: {}".format(firstName))
print("Your last name: {}".format(lastName))
