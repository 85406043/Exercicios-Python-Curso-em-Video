"""APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

stringPhrase = str(input("Whrite a sentence: ")).replace(" ", "").upper()

reversePhrase = stringPhrase[::-1]

if stringPhrase == reversePhrase:
  print("Yes! It's a palindrome.")
  print(f"{stringPhrase}\n{reversePhrase}")
else:
  print("No! It's not a palindrome.")
  print(f"{stringPhrase}\n{reversePhrase}")
