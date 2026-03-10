#I need two variables for height and width
height = float(input("Height: "))
width = float(input("Width: "))
#I need to calculate the area
sum_area = height*width
#I need to calculate
liters = sum_area/2
#Show result
print("Your wall has an area de {:.3f}m². Therefore, the amount of paint in liters is {:.3f}L ".format(sum_area, liters))
