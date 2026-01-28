#I need a starting point for the calculation, distance in meters.
meters = int(input("Enter a number in meters: "))
#Then calculation and convert to km, hm, dam, dm, cm, mm.
km = meters/1000
hm = meters/100
dam = meters/10
dm = meters*10
cm = meters*100
mm = meters*1000
#Then show it on the terminal.
print("KM: {}km".format(km))
print("HM: {}hm".format(hm))
print("DAM: {}dam".format(dam))
print("DM: {}dm".format(dm))
print("CM: {}cm".format(cm))
print("MM: {}mm".format(mm))
