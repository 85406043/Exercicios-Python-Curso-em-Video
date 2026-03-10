name = input("Enter a name: ")
#parameters
uppercase = name.upper()
lowercase = name.lower()
remove_space = "".join(name.split())#name.replace(" ", "")
counting_letters = name.split()[0]
#show
print("Result: \nUppercase: {}\nLowercase: {}\nNo spaces: {}\nNumber of Letters: {}".format(uppercase, lowercase, len(remove_space), len(counting_letters)))
