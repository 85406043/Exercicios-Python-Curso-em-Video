#Enter text
city = input("Name of your hometown: ").upper().strip()
#Module
module = city.startswith("SANTO")
#Show
print("{}".format(module))#print(city[:5].upper() == "SANTO")
