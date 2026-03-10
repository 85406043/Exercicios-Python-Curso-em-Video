#enter name
name = input("Enter your full name: ").upper()
#module or script
check = name.find("SILVA") != -1 # check = "SILVA" in name
#show result
print("Does your name have a Silva? {}".format(check))
