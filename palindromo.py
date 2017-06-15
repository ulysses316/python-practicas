def palindromo(palabra):
   palabra1=(palabra[::-1])
   if palabra==palabra1:
     print("Son iguales")
   else:
     print("No son iguales")

palindromo("bob")
