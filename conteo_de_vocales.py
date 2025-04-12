cadena = "Hola Mundo"
vocales = "aeiouAEIOU"
contador = sum(1 for letra in cadena if letra in vocales)
print("Numero de Vocales: ", contador )
