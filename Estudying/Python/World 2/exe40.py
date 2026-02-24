#i need two notes
firstNote = float(input("Type the first note: "))
secondNote = float(input("Type the second note: "))
calcNotes = (firstNote + secondNote) / 2
#conditions
if calcNotes < 7:
  print(f"Note: {calcNotes}")
  print("Study more next time.")
elif calcNotes <= 7.99:
  print(f"Note: {calcNotes}")
  print("You're average, but you can do better!")
elif calcNotes >= 8:
  print(f"Note: {calcNotes}")
  print("Congratulations! You're above average! Keep it up!")
